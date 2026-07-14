from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import streamlit as st  # Fix 1: Typo — 'steamlit' → 'streamlit'

load_dotenv()

st.header("Research Tool")

user_input = st.text_input("Enter your prompt", key="question")

# Fix 2: Correct button syntax — use 'if st.button(...):'
if st.button("Summerize"):
    result= model.invoke(user_input)
    st.text("some random text") 
    st.write(result.content)  # Fix 3: Correct method to display result content