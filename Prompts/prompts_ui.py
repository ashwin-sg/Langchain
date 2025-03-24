from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.header("Research Tool")

user_input = st.text_input('Enter your prompt')

if st.button('Submit'):
    result = model.invoke(user_input)
    st.write(result.content)