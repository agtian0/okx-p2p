import os
import sys
import json
import time
import hmac
import hashlib
import base64
import urllib.request
import urllib.error
import urllib.parse
from dotenv import load_dotenv

load_dotenv()

OKX_API_KEY = os.getenv("OKX_API_KEY")
OKX_SECRET = os.getenv("OKX_SECRET")
OKX_PASSPHRASE = os.getenv("OKX_PASSPHRASE")
OKX_BASE_URL = os.getenv("OKX_BASE_URL", "https://www.okx.com")

# Load tool definitions from okx-p2p-mcp.json
def load_tools():
    try:
        with open("okx-p2p-mcp.json", "r", encoding="utf-8") as f:
            config = json.load(f)
        return config["servers"][0]["tools"]
    except Exception as e:
        sys.stderr.write(f"Error loading tools: {e}\n")
        return []

TOOLS = load_tools()

def sign_request(timestamp, method, request_path, body=""):
    """Generate OKX API signature."""
    if body:
        body = json.dumps(body) if isinstance(body, (dict, list)) else body
    message = timestamp + method.upper() + request_path + body
    mac = hmac.new(
        bytes(OKX_SECRET, encoding="utf-8"),
        bytes(message, encoding="utf-8"),
        digestmod=hashlib.sha256,
    )
    return base64.b64encode(mac.digest()).decode()

def call_okx(method, path, params=None):
    """Make authenticated OKX API call."""
    timestamp = str(int(time.time() * 1000))
    body = ""
    query = ""

    if method.upper() == "GET" and params:
        query = "?" + urllib.parse.urlencode(params)
        request_path = path + query
    else:
        request_path = path
        if params:
            body = json.dumps(params)

    signature = sign_request(timestamp, method, request_path, body)

    headers = {
        "OK-ACCESS-KEY": OKX_API_KEY,
        "OK-ACCESS-SIGN": signature,
        "OK-ACCESS-TIMESTAMP": timestamp,
        "OK-ACCESS-PASSPHRASE": OKX_PASSPHRASE,
        "Content-Type": "application/json",
    }

    url = OKX_BASE_URL + path + query
    data = body.encode("utf-8") if body else None

    req = urllib.request.Request(url, data=data, headers=headers, method=method.upper())

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        return json.dumps({"error": f"HTTP {e.code}: {e.read().decode()}"})
    except Exception as e:
        return json.dumps({"error": str(e)})

def execute_tool(tool_name, arguments):
    """Find tool definition and execute the corresponding API call."""
    tool = next((t for t in TOOLS if t["name"] == tool_name), None)
    if not tool:
        return json.dumps({"error": f"Tool {tool_name} not found"})

    endpoint = tool["endpoint"]  # e.g. "POST /api/v5/p2p/ad/create"
    method, path = endpoint.split(" ", 1)

    # Extract params from arguments
    params = {}
    if "body" in tool.get("parameters", {}):
        body_params = tool["parameters"]["body"]
        for key in body_params:
            if key in arguments:
                params[key] = arguments[key]
    if "query" in tool.get("parameters", {}):
        query_params = tool["parameters"]["query"]
        for key in query_params:
            if key in arguments:
                params[key] = arguments[key]

    result = call_okx(method, path, params if method.upper() == "POST" else (params or None))
    return result

def main():
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break

            request = json.loads(line)
            req_id = request.get("id")
            method = request.get("method")
            params = request.get("params", {})

            if method == "initialize":
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "protocolVersion": "2024-11-05",
                        "capabilities": {"tools": {}},
                        "serverInfo": {"name": "okx-p2p-mcp", "version": "1.0.0"},
                    },
                }
            elif method == "tools/list":
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"tools": TOOLS},
                }
            elif method == "tools/call":
                tool_name = params.get("name")
                arguments = params.get("arguments", {})
                result_text = execute_tool(tool_name, arguments)
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [{"type": "text", "text": result_text}]
                    },
                }
            else:
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {"code": -32601, "message": f"Method {method} not found"},
                }

            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error: {e}\n")

if __name__ == "__main__":
    main()