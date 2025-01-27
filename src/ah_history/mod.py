from fastapi import APIRouter, Request, Response, HTTPException
from fastapi.responses import JSONResponse
import os
import json
from lib.providers.commands import command

router = APIRouter()

async def recent_chats(path: str) -> list:
    """Retrieve and sort recent chat sessions from the specified directory.

    Args:
        path (str): Directory path containing chat log files

    Returns:
        list: List of dictionaries containing chat metadata:
              - log_id: Unique identifier for the chat
              - descr: Preview of the chat's first message
              - date: Timestamp of the chat

    Raises:
        Exception: If there are issues accessing or parsing chat files
    """
    try:
        files = []
        for file in os.listdir(path):
            files.append(file)
        files.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)), reverse=True)
        chats = files[:130]
        results = []
        for chat in chats:
            with open(f"{path}/{chat}", "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    continue
                message = data["messages"][0]
                results.append({
                    "log_id": chat[8:-5],
                    "descr": message["content"][:80],
                    "date": os.path.getmtime(f"{path}/{chat}")
                })
        return results
    except Exception as e:
        raise(str(e))

@router.get("/session_list/{agent}")
async def get_session_list(request: Request, agent: str = "/") -> JSONResponse:
    """FastAPI endpoint to retrieve chat session list for a specific agent.

    Args:
        request (Request): FastAPI request object containing user state
        agent (str, optional): Agent identifier. Defaults to "/".

    Returns:
        JSONResponse: JSON array of chat session metadata

    Response format:
        [
            {
                "log_id": "unique_chat_id",
                "descr": "First 80 characters of the chat...",
                "date": 1234567890
            }
        ]
    """
    try:
        user = request.state.user
        dir = f"data/chat/{agent}"
        chat = await recent_chats(dir)
        return JSONResponse(chat)
    except Exception as e:
        return JSONResponse({"error": str(e)})
