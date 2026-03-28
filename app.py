import streamlit as st
from config import APP_TITLE, APP_ICON
from styles import CUSTOM_CSS
from ui_components import init_session, render_hero, render_stats, render_welcome, render_sidebar
from chat_engine import chat


def main():
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon=APP_ICON,
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    init_session()
    render_sidebar()
    render_hero()
    render_stats()

    for msg in st.session_state["messages"]:
        avatar = "🧑‍💻" if msg["role"] == "user" else "💬"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

    render_welcome()

    if prompt := st.chat_input("Ask me anything..."):
        st.session_state["messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="🧑‍💻"):
            st.markdown(prompt)

        with st.chat_message("assistant", avatar="💬"):
            with st.spinner("Thinking..."):
                try:
                    reply = chat(prompt)
                    st.markdown(reply)
                    st.session_state["messages"].append({"role": "assistant", "content": reply})
                    st.session_state["query_count"] += 1
                except Exception as e:
                    err = str(e).lower()
                    if "rate limit" in err or "429" in err:
                        st.warning(
                            "**Rate limit reached.**\n\n"
                            "Open the sidebar and switch to a different model in the settings."
                        )
                    else:
                        st.error(f"Something went wrong: {e}")


if __name__ == "__main__":
    main()
