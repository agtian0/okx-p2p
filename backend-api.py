import os
import sys
import json
import asyncio
import subprocess
from typing import List, Dict, Any, Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import urllib.request
import urllib.parse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="OKX P2P Agent Backend", version="1.0.0")

# Enable CORS
origins = os.getenv("CORS_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# LLM endpoint config
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://api.openai.com/v1")
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")

# Subprocess paths
IMAP_MCP_PATH = os.path.abspath("imap-mcp.py")
OKX_MCP_PATH = os.path.abspath("okx-p2p-mcp-server.py")

# Load OKX skill documentation
def load_skill_docs() -> str:
    try:
        with open("okx-p2p-skill/SKILL.md", "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return "OKX P2P API Skill reference doc could not be loaded."

SKILL_DOCS = load_skill_docs()

class ChatMessage(BaseModel):
    role: str
    content: Optional[str] = None
    name: Optional[str] = None
    tool_calls: Optional[List[Dict[str, Any]]] = None
    tool_call_id: Optional[str] = None

class ChatCompletionRequest(BaseModel):
    model: str = LLM_MODEL
    messages: List[ChatMessage]
    temperature: Optional[float] = 0.7
    stream: Optional[bool] = False
    tools: Optional[List[Dict[str, Any]]] = None
    tool_choice: Optional[Any] = None

class ProcessManager:
    """Manages MCP stdio connections."""
    def __init__(self, script_path: str):
        self.script_path = script_path
        self.process = None

    async def start(self):
        if not self.process:
            self.process = await asyncio.create_subprocess_exec(
                sys.executable,
                self.script_path,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            # Send initialize message
            await self.call("initialize", {"protocolVersion": "2024-11-05"})

    async def call(self, method: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        await self.start()
        req_id = int(time.time() * 1000)
        req = {
            "jsonrpc": "2.0",
            "id": req_id,
            "method": method,
            "params": params or {}
        }

        self.process.stdin.write((json.dumps(req) + "\n").encode())
        await self.process.stdin.drain()

        # Read line response
        line = await self.process.stdout.readline()
        if not line:
            raise Exception("Subprocess died or returned EOF")

        resp = json.loads(line.decode())
        if "error" in resp:
            raise Exception(resp["error"].get("message", "Unknown MCP error"))
        return resp.get("result", {})

    async def stop(self):
        if self.process:
            try:
                self.process.terminate()
                await self.process.wait()
            except Exception:
                pass
            self.process = None

# Create process managers for the MCP servers
import time
imap_mcp = ProcessManager(IMAP_MCP_PATH)
okx_mcp = ProcessManager(OKX_MCP_PATH)

# Expose available tools dynamically to OpenAI format
async def get_all_mcp_tools() -> List[Dict[str, Any]]:
    await imap_mcp.start()
    await okx_mcp.start()

    imap_tools = await imap_mcp.call("tools/list")
    okx_tools = await okx_mcp.call("tools/list")

    openai_tools = []

    # Map IMAP tools
    for tool in imap_tools.get("tools", []):
        openai_tools.append({
            "type": "function",
            "function": {
                "name": f"imap_{tool['name']}",
                "description": f"[Email] {tool['description']}",
                "parameters": tool.get("inputSchema", {})
            }
        })

    # Map OKX tools
    for tool in okx_tools.get("tools", []):
        # We need to construct parameters from query + body params
        properties = {}
        required = []

        # Merge query and body params
        params = tool.get("parameters", {})
        if "query" in params:
            for k, v in params["query"].items():
                properties[k] = {"type": "string" if v == "string" else "number", "description": f"Query param: {k}"}
        if "body" in params:
            for k, v in params["body"].items():
                properties[k] = {"type": "string" if v == "string" else "number", "description": f"Body param: {k}"}

        # Copy required fields
        required = tool.get("required", [])

        openai_tools.append({
            "type": "function",
            "function": {
                "name": f"okx_{tool['name']}",
                "description": f"[OKX P2P] {tool['description']}",
                "parameters": {
                    "type": "object",
                    "properties": properties,
                    "required": required
                }
            }
        })

    return openai_tools

async def call_mcp_tool(func_name: str, args: Dict[str, Any]) -> str:
    """Route tool call to appropriate MCP server."""
    if func_name.startswith("imap_"):
        real_name = func_name[5:]
        res = await imap_mcp.call("tools/call", {"name": real_name, "arguments": args})
        content = res.get("content", [])
        return content[0].get("text", "") if content else ""
    elif func_name.startswith("okx_"):
        real_name = func_name[4:]
        res = await okx_mcp.call("tools/call", {"name": real_name, "arguments": args})
        content = res.get("content", [])
        return content[0].get("text", "") if content else ""
    else:
        raise ValueError(f"Unknown tool prefix: {func_name}")

@app.on_event("startup")
async def startup_event():
    await imap_mcp.start()
    await okx_mcp.start()

@app.on_event("shutdown")
async def shutdown_event():
    await imap_mcp.stop()
    await okx_mcp.stop()

@app.post("/v1/chat/completions")
async def chat_completions(req: ChatCompletionRequest):
    # Inject OKX Skill details in System prompt if not present
    messages = [m.dict(exclude_none=True) for m in req.messages]

    has_system = any(m["role"] == "system" for m in messages)
    system_prompt = (
        "You are an expert OKX P2P trading agent. You have tools to read/send emails (Gmail) "
        "and complete P2P trades. Always be careful with funds. Confirm details before actions.\n\n"
        f"OKX P2P Workflows:\n{SKILL_DOCS}"
    )

    if not has_system:
        messages.insert(0, {"role": "system", "content": system_prompt})
    else:
        for m in messages:
            if m["role"] == "system":
                m["content"] = system_prompt + "\n\n" + (m.get("content") or "")

    # Inject our dynamic tools if LLM is asking for them
    tools = await get_all_mcp_tools()

    # Forward request to custom OpenAI-compatible API
    payload = {
        "model": req.model,
        "messages": messages,
        "temperature": req.temperature,
        "tools": tools,
    }

    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}",
        "Content-Type": "application/json"
    }

    req_url = f"{LLM_BASE_URL}/chat/completions"
    data = json.dumps(payload).encode("utf-8")

    http_req = urllib.request.Request(req_url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(http_req, timeout=60) as resp:
            resp_body = resp.read().decode("utf-8")
            return json.loads(resp_body)
    except urllib.error.HTTPError as e:
        error_msg = e.read().decode()
        sys.stderr.write(f"LLM API Error: {error_msg}\n")
        raise HTTPException(status_code=e.code, detail=error_msg)
    except Exception as e:
        sys.stderr.write(f"Error calling LLM API: {e}\n")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/tool/call")
async def call_tool(req: Request):
    """Direct route for front-end or backend to call MCP tools directly."""
    body = await req.json()
    name = body.get("name")
    arguments = body.get("arguments", {})
    if not name:
        raise HTTPException(status_code=400, detail="Missing name parameter")
    try:
        result = await call_mcp_tool(name, arguments)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/tools")
async def list_tools():
    """List all available tools in OpenAI format."""
    try:
        tools = await get_all_mcp_tools()
        return {"tools": tools}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health():
    return {"status": "ok", "mcp_servers": {"imap": "running", "okx": "running"}}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend-api:app", host="0.0.0.0", port=8000, reload=True)
