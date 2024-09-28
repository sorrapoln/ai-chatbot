import streamlit as st
import google.generativeai as genai

st.title("🥨 Food suggestion Chatbot")
st.subheader("Conversation")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


gemini_api_key = st.text_input("API Key : ", type = "password")

if gemini_api_key :
    try:
        genai.configure(api_key = gemini_api_key)
        model = genai.GenerativeModel("gemini-pro")
        st.success("Get API Key!!")
    except Exception as e:
        st.error("Error while setting up gemini model")
for msg in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(msg[0])
    with st.chat_message("assistant"):
        st.markdown(msg[1])

if prompt := st.chat_input("Type message : "):
    if model:
        try:
            full_prompt = "Context : You a plan advisor. Please suggest travel plan for user " + ", User Input : " + prompt
            response = model.generate_content(full_prompt)
            assistant_ans = response.text
        except:
            assistant_ans = prompt + " Ohm"
    st.session_state.chat_history.append([prompt, assistant_ans])
    st.chat_message("user").markdown(prompt)
    st.chat_message("assistant").markdown(assistant_ans)

