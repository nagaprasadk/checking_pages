import streamlit as st
from langchain_openai import OpenAI

# 🔑 Direct API key (replace with your actual key)
OPENAI_API_KEY = "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"

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
