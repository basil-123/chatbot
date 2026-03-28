import os
from dotenv import load_dotenv

# Ensure we always get the latest .env changes
load_dotenv(override=True)

APP_TITLE = "NexusChat AI"
APP_ICON = "💬"

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

AVAILABLE_MODELS = [
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
    "llama3-70b-8192",
    "llama3-8b-8192",
    "mixtral-8x7b-32768",
    "gemma2-9b-it",
]

MEMORY_WINDOW = 10
DEFAULT_MODEL = AVAILABLE_MODELS[0]
