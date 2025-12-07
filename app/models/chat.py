from typing import Optional
from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    user_id: Optional[str] = Field(
        default=None,
        description="Optional user identifier for sessions."
    )
    message: str = Field(..., min_length=1, description="User message text.")

class ChatResponse(BaseModel):
    reply: str
    is_crisis: bool = False
