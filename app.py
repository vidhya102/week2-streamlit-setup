import streamlit as st

st.title("Week 2 Task - Streamlit Setup")
st.write("Hello! Streamlit is successfully installed and running.")

name = st.text_input("Enter your name")
if name:
    st.success(f"Hello {name}, your Streamlit app is working!")

