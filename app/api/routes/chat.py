from fastapi import APIRouter, HTTPException
from app.models.chat import ChatRequest, ChatResponse
from app.services.llm_client import call_llm
from app.services.safety import (
    is_crisis_message,
    crisis_reply,
    sanitize_model_reply,
)

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("", response_model=ChatResponse)
def chat_endpoint(payload: ChatRequest) -> ChatResponse:
    user_msg = payload.message.strip()
    if not user_msg:
        raise HTTPException(status_code=400, detail="Empty message.")

    # 1. Crisis detection BEFORE calling model
    if is_crisis_message(user_msg):
        return ChatResponse(
            reply=crisis_reply(),
            is_crisis=True,
        )

    # 2. Normal flow: call model
    try:
        raw_reply = call_llm(user_msg)
    except Exception as e:
        # on failure, do NOT expose exception details
        raise HTTPException(
            status_code=500,
            detail="Internal error when generating response.",
        ) from e

    # 3. Outgoing sanitization (defensive)
    safe_reply, modified = sanitize_model_reply(raw_reply)
    return ChatResponse(
        reply=safe_reply,
        is_crisis=False,
    )
