import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)
import warnings
import sys

# Custom CSS styling for the app
st.markdown("""
<style>
    /* Existing styles */
    .main {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background-color: #2d2d2d;
    }
    .stTextInput textarea {
        color: #ffffff !important;
    }
    
    /* Add these new styles for select box */
    .stSelectbox div[data-baseweb="select"] {
        color: white !important;
        background-color: #3d3d3d !important;
    }
    
    .stSelectbox svg {
        fill: white !important;
    }
    
    .stSelectbox option {
        background-color: #2d2d2d !important;
        color: white !important;
    }
    
    /* For dropdown menu items */
    div[role="listbox"] div {
        background-color: #2d2d2d !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)
st.title("🧠 DeepSeek Code Companion Build by Lokendra Singh")
st.caption("🚀 Your AI Pair Programmer with Debugging Superpowers")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    selected_model = st.selectbox(
        "Choose Model",
        ["deepseek-r1:1.5b", "deepseek-r1:3b", "deepseek-r1:7b", "deepseek-r1:8b"],
        index=0
    )
    st.divider()
    st.markdown("### Model Capabilities")
    st.markdown("""
    - 🐍 Code genaration
    - 🐞 Debugging Assistant
    - 📝 Documentation
    """)
    st.divider()
    
    st.markdown("### 🔗 Resources")
    st.markdown("""
    - [Ollama Documentation](https://ollama.ai/)
    - [LangChain Guides](https://python.langchain.com/)
    - [DeepSeek GitHub](https://github.com/deepseek-ai)
    """)

# Initialize chat engine with selected model(Deepseek)
llm_engine = ChatOllama(
    model=selected_model,
    base_url="http://localhost:11434",
    temperature=0.3,
    streaming=True
)

# System prompt configuration
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an expert AI coding assistant. Provide concise, correct solutions "
    "with strategic print statements for debugging. Always respond in English."
)

# Session state management
if "message_log" not in st.session_state:
    st.session_state.message_log = [{
        "role": "ai", 
        "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"
    }]

# Display chat messages
def display_chat_history():
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Build the prompt chain
def build_prompt_chain():
    prompt_sequence = [system_prompt]
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
    return ChatPromptTemplate.from_messages(prompt_sequence)

# Generate AI response with streaming
def generate_response():
    prompt_chain = build_prompt_chain()
    processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
    return processing_pipeline.stream({})

# Display chat history
display_chat_history()

# Handle user input
user_query = st.chat_input("Type your coding question here...")

if user_query:
    # Add user message to history
    st.session_state.message_log.append({"role": "user", "content": user_query})
    
    # Display user message immediately
    with st.chat_message("user"):
        st.markdown(user_query)
    
    # Create placeholder for assistant response
    with st.chat_message("ai"):
        response_placeholder = st.empty()
        response_placeholder.markdown('<div class="typing-indicator">Generating<span class="dot"></span><span class="dot"></span><span class="dot"></span></div>', unsafe_allow_html=True)
    
    # Generate and stream response
    full_response = ""
    for chunk in generate_response():
        full_response += chunk
        response_placeholder.markdown(full_response + "▌")
    
    # Update final response
    response_placeholder.markdown(full_response)
    
    # Add assistant response to history
    st.session_state.message_log.append({"role": "ai", "content": full_response})