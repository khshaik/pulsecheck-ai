import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="PulseCheck AI", page_icon="🚀")

# 1. Setup API Key
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Please add your GOOGLE_API_KEY to Streamlit Secrets.")
    st.stop()

# 2. Define the Master Prompt (The Rulebook)
SYSTEM_PROMPT = """
[PASTE YOUR ENTIRE MASTER PROMPT HERE]
"""

# 3. Initialize the Model with System Instructions
# This prevents the bot from "repeating" the prompt to you
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction=SYSTEM_PROMPT
)

st.title("🚀 PulseCheck AI")

# 4. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Starting the conversation
    initial_text = "🚀 *Welcome to PulseCheck AI.* I'm ready to begin. What is the *Target Role and Company* you are aiming for?"
    st.session_state.messages.append({"role": "assistant", "content": initial_text})

# 5. Display History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. Handle User Input
if prompt := st.chat_input("Enter your response..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 7. Generate Response using Chat Session
    # We pass the history but NOT the system prompt here (it's already in the model)
    chat = model.start_chat(history=[
        {"role": m["role"] if m["role"] == "user" else "model", "parts": [m["content"]]} 
        for m in st.session_state.messages[:-1] # excludes the latest prompt
    ])
    
    response = chat.send_message(prompt)
    
    # Show assistant message
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})