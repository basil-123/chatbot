# Chatly

Lightweight, modular conversational assistant built with LangChain and Groq LLMs.  
Chatly provides a reusable chat engine with sliding-window memory and simple Streamlit-ready UI.

## Features
- Context-aware conversation using ConversationBufferWindowMemory
- Groq model integration via langchain_groq.ChatGroq
- Config-driven model selection and memory window (config.py / .env)
- Frontend-agnostic: ready for Streamlit or other UIs

## Quick Start

Prerequisites
- Python 3.8+
- Groq API key

Install
```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install langchain langchain_groq python-dotenv streamlit
```

Configuration
1. Create a `.env` in the project root:
````text
GROQ_API_KEY=your_groq_api_key_here
