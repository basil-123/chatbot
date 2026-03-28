CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    * { font-family: 'Inter', sans-serif; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }

    /* Main background & Global Text Color */
    .stApp {
        background: linear-gradient(135deg, #0a0a0f 0%, #0f0c29 50%, #100c2a 100%);
        min-height: 100vh;
        color: #f3f4f6 !important;
    }
    
    /* Force markdown text globally */
    .stMarkdown, .stMarkdown p, .stMarkdown span, .stMarkdown div {
        color: #f3f4f6 !important;
    }

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d0b1e 0%, #130f30 60%, #0f0c29 100%);
        border-right: 1px solid rgba(147, 51, 234, 0.15);
        padding-top: 2rem;
    }

    section[data-testid="stSidebar"] .stMarkdown h1,
    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3 {
        color: #e0d7ff !important;
        font-weight: 600;
        font-size: 1.5rem !important;
    }
    
    section[data-testid="stSidebar"] .stMarkdown p,
    section[data-testid="stSidebar"] .stMarkdown li {
        color: #9d8ec7 !important;
        font-size: 1.1rem !important;
    }

    /* Hero section */
    .hero-wrap {
        text-align: center;
        padding: 5vh 20px 3vh;
    }
    .hero-title {
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 700;
        background: linear-gradient(135deg, #a78bfa 0%, #818cf8 40%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 12px;
        animation: slideDown 0.7s ease-out;
    }
    .hero-sub {
        font-size: clamp(1.1rem, 2vw, 1.4rem);
        color: #9d8ec7;
        font-weight: 300;
        letter-spacing: 0.5px;
        animation: slideUp 0.7s ease-out;
    }

    /* Stats Row */
    .stat-row {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 24px;
        padding: 20px 10px;
        margin-bottom: 2vh;
    }
    .stat-box {
        text-align: center;
        background: rgba(139, 92, 246, 0.08);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 16px;
        padding: 16px 32px;
        min-width: 140px;
        flex: 1 1 auto;
        max-width: 200px;
        transition: all 0.3s ease;
    }
    .stat-box:hover { 
        border-color: rgba(139, 92, 246, 0.4); 
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(139, 92, 246, 0.15);
    }
    .stat-num {
        font-size: 2.2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #a78bfa, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .stat-lbl {
        font-size: 0.85rem;
        color: #9ca3af;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-top: 4px;
    }

    /* Welcome Card */
    .welcome-wrap {
        text-align: center;
        padding: 60px 40px;
        background: rgba(255,255,255,0.02);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(139,92,246,0.25);
        border-radius: 24px;
        margin: 40px auto;
        max-width: 700px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }
    .welcome-icon { font-size: 4rem; margin-bottom: 20px; }
    .welcome-title { color: #ddd6fe; font-size: 1.8rem; font-weight: 600; margin-bottom: 12px; }
    .welcome-desc { color: #a1a1aa; font-size: 1.15rem; line-height: 1.7; }
    
    .feat-grid {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 12px;
        margin-top: 30px;
    }
    .feat-pill {
        background: rgba(139,92,246,0.1);
        border: 1px solid rgba(139,92,246,0.25);
        border-radius: 12px;
        padding: 8px 18px;
        font-size: 0.95rem;
        color: #c4b5fd;
        font-weight: 500;
    }

    /* Inputs & Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #7c3aed 0%, #6d28d9 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 10px 24px !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:hover {
        box-shadow: 0 6px 20px rgba(124, 58, 237, 0.5) !important;
        transform: translateY(-2px) !important;
    }

    .stTextInput > div > div > input,
    .stSelectbox > div > div,
    /* Custom Scrollbar for professional feel */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    ::-webkit-scrollbar-track {
        background: transparent; 
    }
    ::-webkit-scrollbar-thumb {
        background: rgba(139, 92, 246, 0.3); 
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(139, 92, 246, 0.6); 
    }

    /* Fixed Bottom Chat Input Styling */
    .stChatInputContainer {
        padding-bottom: 2rem !important;
        background: transparent !important;
    }
    .stChatInput {
        background: transparent !important;
        background-color: transparent !important;
    }
    /* The wrapping div */
    div[data-testid="stChatInput"] {
        background: transparent !important;
        background-color: transparent !important;
    }
    .stChatInput > div {
        background: rgba(15, 12, 41, 0.8) !important;
        backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(139,92,246,0.3) !important;
        border-radius: 18px !important;
        color: #e0d7ff !important;
        font-size: 1.15rem !important;
        padding: 6px 16px !important;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3) !important;
    }
    .stChatInput > div:focus-within {
        border-color: #a78bfa !important;
        box-shadow: 0 0 0 2px rgba(167, 139, 250, 0.4), 0 8px 32px rgba(0,0,0,0.3) !important;
        background: rgba(15, 12, 41, 0.95) !important;
    }

    /* Override input text colors to ensure visibility */
    .stChatInput textarea {
        color: #f3f4f6 !important;
        background: transparent !important;
        background-color: transparent !important;
    }
    .stChatInput button {
        color: #a78bfa !important;
    }
    .stChatInput button:hover {
        color: #ddd6fe !important;
        background: rgba(139,92,246,0.2) !important;
    }

    /* Chat Messages */
    div[data-testid="stChatMessage"] {
        background: rgba(255,255,255,0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(139,92,246,0.15);
        border-radius: 18px;
        padding: 20px 24px;
        margin-bottom: 16px;
        font-size: 1.15rem !important;
        line-height: 1.6 !important;
        color: #f3f4f6 !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    div[data-testid="stChatMessage"] .stMarkdown p {
        font-size: 1.15rem !important;
        color: #f3f4f6 !important;
    }

    /* Removes the empty space at top of streamlit */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 10rem !important;
        max-width: 900px !important;
    }

    /* Animations */
    @keyframes slideDown { from { opacity: 0; transform: translateY(-24px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes slideUp { from { opacity: 0; transform: translateY(24px); } to { opacity: 1; transform: translateY(0); } }
</style>
"""
