from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",  # or any other model
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

st.header("Research Tool")

user_input = st.text_input("Enter your prompt", key="question")

if st.button("Summarize"):
    if user_input:
        result = model.invoke(user_input)
        st.write(result.content)
    else:
        st.warning("Please enter a prompt first!")