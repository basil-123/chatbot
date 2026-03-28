import streamlit as st
from config import APP_TITLE, AVAILABLE_MODELS, DEFAULT_MODEL
from chat_engine import build_chain, reset_chain


def init_session():
    defaults = {
        "messages": [],
        "chain": None,
        "query_count": 0,
        "selected_model": DEFAULT_MODEL,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def render_hero():
    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-title">Chatly</div>
        <div class="hero-sub">Context-aware conversations that remember what matters ✨</div>
    </div>
    """, unsafe_allow_html=True)


def render_stats():
    turns = len(st.session_state["messages"]) // 2
    st.markdown(f"""
    <div class="stat-row">
        <div class="stat-box">
            <div class="stat-num">{len(st.session_state["messages"])}</div>
            <div class="stat-lbl">Messages</div>
        </div>
        <div class="stat-box">
            <div class="stat-num">{turns}</div>
            <div class="stat-lbl">Turns</div>
        </div>
        <div class="stat-box">
            <div class="stat-num">{st.session_state["query_count"]}</div>
            <div class="stat-lbl">Queries</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_welcome():
    if st.session_state["messages"]:
        return
    st.markdown("""
    <div class="welcome-wrap">
        <div class="welcome-icon">💬</div>
        <div class="welcome-title">Welcome to Chatly</div>
        <div class="welcome-desc">
            Ask me anything. I remember the full context of our conversation,
            so feel free to use follow-up questions without re-explaining what you mean.
        </div>
        <div class="feat-grid">
            <span class="feat-pill">Context Retention</span>
            <span class="feat-pill">Follow-up Understanding</span>
            <span class="feat-pill">Multi-turn Dialogue</span>
            <span class="feat-pill">No Hallucinations</span>
            <span class="feat-pill">Token Optimized</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_sidebar():
    with st.sidebar:
        st.markdown(f"## {APP_TITLE} 💬")
        st.divider()
        st.markdown("### ⚙️ Settings")

        new_model = st.selectbox(
            "AI Model",
            options=AVAILABLE_MODELS,
            index=AVAILABLE_MODELS.index(st.session_state["selected_model"])
                  if st.session_state["selected_model"] in AVAILABLE_MODELS else 0,
        )
        if new_model != st.session_state["selected_model"]:
            st.session_state["selected_model"] = new_model
            st.session_state["chain"] = None
            st.rerun()

        st.divider()

        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state["messages"] = []
            st.session_state["query_count"] = 0
            reset_chain()
            st.rerun()

        st.divider()
        st.markdown("### 📌 How It Works")
        st.caption(
            "Chatly maintains a sliding window of your last 10 exchanges. "
            "Older messages are dropped to stay within token limits while keeping "
            "the most recent context fully intact."
        )
