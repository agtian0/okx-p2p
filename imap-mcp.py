import os
import sys
import json
import imaplib
import smtplib
import email
from email.mime.text import MIMEText
from email.header import decode_header
from typing import Dict, Any, List
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD") # Gmail App Password
IMAP_HOST = os.getenv("IMAP_HOST", "imap.gmail.com")
IMAP_PORT = int(os.getenv("IMAP_PORT", "993"))
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))

def connect_imap():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT)
        mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        return mail
    except Exception as e:
        sys.stderr.write(f"IMAP Connection failed: {e}\n")
        return None

def connect_smtp():
    try:
        server = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT)
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        return server
    except Exception as e:
        sys.stderr.write(f"SMTP Connection failed: {e}\n")
        return None

def decode_mime_words(s):
    if not s:
        return ""
    clean_parts = []
    try:
        for word, encoding in decode_header(s):
            if isinstance(word, bytes):
                clean_parts.append(word.decode(encoding or "utf-8", errors="ignore"))
            else:
                clean_parts.append(str(word))
    except Exception:
        return str(s)
    return "".join(clean_parts)

def clean_body(body_bytes, charset):
    try:
        return body_bytes.decode(charset or "utf-8", errors="ignore")
    except Exception:
        return body_bytes.decode("latin1", errors="ignore")

def get_email_body(msg):
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            if content_type == "text/plain" and "attachment" not in content_disposition:
                charset = part.get_content_charset()
                body += clean_body(part.get_payload(decode=True), charset)
    else:
        charset = msg.get_content_charset()
        body = clean_body(msg.get_payload(decode=True), charset)
    return body

# MCP protocol tools
TOOLS = [
    {
        "name": "list_emails",
        "description": "List recent emails from Inbox",
        "inputSchema": {
            "type": "object",
            "properties": {
                "limit": {"type": "integer", "description": "Number of emails to return (default 10)", "default": 10},
                "folder": {"type": "string", "description": "Folder/label name (default INBOX)", "default": "INBOX"}
            }
        }
    },
    {
        "name": "read_email",
        "description": "Read complete email details by UID/ID",
        "inputSchema": {
            "type": "object",
            "properties": {
                "email_id": {"type": "string", "description": "UID of the email"},
                "folder": {"type": "string", "description": "Folder/label name", "default": "INBOX"}
            },
            "required": ["email_id"]
        }
    },
    {
        "name": "search_emails",
        "description": "Search emails by criteria (e.g. from, subject, body text)",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query. E.g., 'FROM \"okx\"', 'SUBJECT \"P2P\"', 'UNSEEN'"},
                "folder": {"type": "string", "description": "Folder/label name", "default": "INBOX"}
            },
            "required": ["query"]
        }
    },
    {
        "name": "send_email",
        "description": "Send an email via SMTP",
        "inputSchema": {
            "type": "object",
            "properties": {
                "to": {"type": "string", "description": "Recipient email address"},
                "subject": {"type": "string", "description": "Email subject"},
                "body": {"type": "string", "description": "Email body content (text/plain)"}
            },
            "required": ["to", "subject", "body"]
        }
    }
]

def handle_list_emails(limit: int = 10, folder: str = "INBOX") -> str:
    mail = connect_imap()
    if not mail:
        return json.dumps({"error": "Failed to connect to IMAP server"})

    try:
        mail.select(folder)
        status, messages = mail.search(None, "ALL")
        if status != "OK":
            return json.dumps({"error": "Failed to search inbox"})

        mail_ids = messages[0].split()
        mail_ids = mail_ids[-limit:]  # get recent ones
        mail_ids.reverse()

        email_list = []
        for mid in mail_ids:
            status, data = mail.fetch(mid, "(RFC822.SIZE BODY[HEADER.FIELDS (SUBJECT FROM DATE)])")
            if status == "OK" and data:
                raw_header = data[0][1]
                msg = email.message_from_bytes(raw_header)
                email_list.append({
                    "id": mid.decode(),
                    "subject": decode_mime_words(msg.get("Subject")),
                    "from": decode_mime_words(msg.get("From")),
                    "date": msg.get("Date")
                })
        return json.dumps(email_list, indent=2)
    except Exception as e:
        return json.dumps({"error": f"Error listing emails: {e}"})
    finally:
        mail.logout()

def handle_read_email(email_id: str, folder: str = "INBOX") -> str:
    mail = connect_imap()
    if not mail:
        return json.dumps({"error": "Failed to connect to IMAP server"})

    try:
        mail.select(folder)
        status, data = mail.fetch(email_id.encode(), "(RFC822)")
        if status != "OK" or not data:
            return json.dumps({"error": f"Failed to fetch email with ID {email_id}"})

        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        email_data = {
            "id": email_id,
            "subject": decode_mime_words(msg.get("Subject")),
            "from": decode_mime_words(msg.get("From")),
            "to": decode_mime_words(msg.get("To")),
            "date": msg.get("Date"),
            "body": get_email_body(msg)
        }
        return json.dumps(email_data, indent=2)
    except Exception as e:
        return json.dumps({"error": f"Error reading email {email_id}: {e}"})
    finally:
        mail.logout()

def handle_search_emails(query: str, folder: str = "INBOX") -> str:
    mail = connect_imap()
    if not mail:
        return json.dumps({"error": "Failed to connect to IMAP server"})

    try:
        mail.select(folder)
        status, messages = mail.search(None, query)
        if status != "OK":
            return json.dumps({"error": f"Failed search for: {query}"})

        mail_ids = messages[0].split()
        email_list = []
        for mid in mail_ids[-20:]:  # limit to 20 search results
            status, data = mail.fetch(mid, "(RFC822.SIZE BODY[HEADER.FIELDS (SUBJECT FROM DATE)])")
            if status == "OK" and data:
                raw_header = data[0][1]
                msg = email.message_from_bytes(raw_header)
                email_list.append({
                    "id": mid.decode(),
                    "subject": decode_mime_words(msg.get("Subject")),
                    "from": decode_mime_words(msg.get("From")),
                    "date": msg.get("Date")
                })
        return json.dumps(email_list, indent=2)
    except Exception as e:
        return json.dumps({"error": f"Error searching emails: {e}"})
    finally:
        mail.logout()

def handle_send_email(to: str, subject: str, body: str) -> str:
    server = connect_smtp()
    if not server:
        return json.dumps({"error": "Failed to connect to SMTP server"})

    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to

        server.sendmail(EMAIL_ADDRESS, [to], msg.as_string())
        return json.dumps({"success": True, "message": f"Email sent successfully to {to}"})
    except Exception as e:
        return json.dumps({"error": f"Error sending email: {e}"})
    finally:
        server.quit()

# Stdio communication loop
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

            # MCP Methods
            if method == "initialize":
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "protocolVersion": "2024-11-05",
                        "capabilities": {
                            "tools": {}
                        },
                        "serverInfo": {
                            "name": "imap-mcp",
                            "version": "1.0.0"
                        }
                    }
                }
            elif method == "tools/list":
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": TOOLS
                    }
                }
            elif method == "tools/call":
                tool_name = params.get("name")
                arguments = params.get("arguments", {})

                result_content = ""
                if tool_name == "list_emails":
                    result_content = handle_list_emails(
                        limit=arguments.get("limit", 10),
                        folder=arguments.get("folder", "INBOX")
                    )
                elif tool_name == "read_email":
                    result_content = handle_read_email(
                        email_id=arguments.get("email_id"),
                        folder=arguments.get("folder", "INBOX")
                    )
                elif tool_name == "search_emails":
                    result_content = handle_search_emails(
                        query=arguments.get("query"),
                        folder=arguments.get("folder", "INBOX")
                    )
                elif tool_name == "send_email":
                    result_content = handle_send_email(
                        to=arguments.get("to"),
                        subject=arguments.get("subject"),
                        body=arguments.get("body")
                    )
                else:
                    response = {
                        "jsonrpc": "2.0",
                        "id": req_id,
                        "error": {
                            "code": -32601,
                            "message": f"Tool {tool_name} not found"
                        }
                    }
                    sys.stdout.write(json.dumps(response) + "\n")
                    sys.stdout.flush()
                    continue

                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [
                            {
                                "type": "text",
                                "text": result_content
                            }
                        ]
                    }
                }
            else:
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {
                        "code": -32601,
                        "message": f"Method {method} not found"
                    }
                }

            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()

        except Exception as e:
            sys.stderr.write(f"Error in main loop: {e}\n")

if __name__ == "__main__":
    main()
