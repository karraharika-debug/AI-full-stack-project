import streamlit as st
st.title("LOGIN PAGE")
st.write("Username:")
name=st.text_input("",placeholder="Enter your name....")

st.write("hello",name)
if st.button("click here"):
    st.write("Completed")

