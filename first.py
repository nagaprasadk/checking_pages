import streamlit as st
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize the LLM
llm = OpenAI(model='gpt-3.5-turbo-instruct')

st.title("Simple LangChain + OpenAI App")

# Text input
prompt = st.text_input("Enter your question:")

# Button to run
if st.button("Ask"):
    if prompt.strip() == "":
        st.warning("Please enter a question.")
    else:
        # Call the model
        result = llm.invoke(prompt)
        st.success("Response:")
        st.write(result)
