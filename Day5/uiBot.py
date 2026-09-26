import ollama
import streamlit as st
if "messages" not in st.session_state:
    st.session_state.messages = []
question = st.chat_input("You: ")
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
if question:
    with st.chat_message("user"):
        st.write("user: ", question)
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )
    with st.spinner("Thinking..."):
        response = ollama.chat(
            model="llama3.2:3b",
            messages=st.session_state.messages
        )
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response["message"]["content"]
        }
    )
    with st.chat_message("assistant"):
        st.write("assistent: ", response["message"]["content"])

    st.write("AI:", response["message"]["content"])
with st.sidebar:
    uploaded_file = st.file_uploader("Upload a file...")
    if uploaded_file:
        st.write("File uploaded successfullyy!!")
        context = uploaded_file.read().decode("utf-8")
        st.write(context)