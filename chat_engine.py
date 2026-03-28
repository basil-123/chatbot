import streamlit as st
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from config import GROQ_API_KEY, MEMORY_WINDOW, DEFAULT_MODEL


PROMPT_TEMPLATE = PromptTemplate(
    input_variables=["history", "input"],
    template="""You are NexusChat AI, a helpful and intelligent conversational assistant.

Rules you must always follow:
1. Always maintain context from the conversation history. If the user refers to something mentioned earlier (like "it", "that", "its"), resolve it from the previous messages.
2. Never repeat the same answer you already gave. Build on and extend prior responses.
3. If you are not confident about something, say so clearly and ask the user for clarification instead of guessing.
4. Do not make up facts or information you are uncertain about.
5. Keep responses clear, concise, and well-structured using markdown where it helps.
6. When continuing a topic from earlier in the conversation, acknowledge the connection naturally.

Current conversation:
{history}
Human: {input}
AI:"""
)


def build_chain():
    model = st.session_state.get("selected_model", DEFAULT_MODEL)

    llm = ChatGroq(model=model, temperature=0.4, api_key=GROQ_API_KEY)

    memory = ConversationBufferWindowMemory(
        k=MEMORY_WINDOW,
        human_prefix="Human",
        ai_prefix="AI",
    )

    return ConversationChain(
        llm=llm,
        memory=memory,
        prompt=PROMPT_TEMPLATE,
        verbose=False,
    )


def chat(user_input: str) -> str:
    if "chain" not in st.session_state or st.session_state["chain"] is None:
        st.session_state["chain"] = build_chain()

    chain = st.session_state["chain"]
    response = chain.predict(input=user_input)
    return response.strip()


def reset_chain():
    st.session_state["chain"] = build_chain()
