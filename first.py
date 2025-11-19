import streamlit as st
from langchain_openai import OpenAI

# 🔑 Direct API key (replace with your actual key)
OPENAI_API_KEY = "your_api_key_here"

# Initialize the model
llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    openai_api_key=OPENAI_API_KEY
)

# Streamlit UI
st.title("Simple LangChain + OpenAI App")

prompt = st.text_input("Enter your question:")

if st.button("Ask"):
    if prompt.strip() == "":
        st.warning("Please enter a question.")
    else:
        result = llm.invoke(prompt)
        st.success("Response:")
        st.write(result)
