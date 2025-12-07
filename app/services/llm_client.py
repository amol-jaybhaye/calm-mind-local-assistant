import requests
from app.core.config import settings
from app.core.prompts import SYSTEM_PROMPT

def call_llm(user_message: str) -> str:
    """
    Call local Ollama chat endpoint with system + single user message.

    We intentionally keep context minimal because of your 8GB RAM:
    - No long conversation history.
    - You can manage state in your DB later if needed.
    """
    payload = {
        "model": settings.MODEL_NAME,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        "stream": False,
    }

    resp = requests.post(
        settings.OLLAMA_URL,
        json=payload,
        timeout=120,
    )
    resp.raise_for_status()

    data = resp.json()
    # Ollama response structure: {"message": {"role": "...", "content": "..."}, ...}
    return data["message"]["content"]
