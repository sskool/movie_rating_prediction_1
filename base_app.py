import streamlit as streamlit

st.title("My First Streamlit App")

name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")