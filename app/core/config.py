import os
from dotenv import load_dotenv

# Load .env if present
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
env_path = os.path.join(BASE_DIR, ".env")
if os.path.exists(env_path):
    load_dotenv(env_path)

class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "Mental Health Assistant")
    OLLAMA_URL: str = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")
    MODEL_NAME: str = os.getenv(
        "MODEL_NAME",
        "tinyllama:1.1b-chat-v1-q4_0",  # good default for 8GB RAM
    )
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

settings = Settings()
