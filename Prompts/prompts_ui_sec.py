from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()
st.header("Research Tool")

paper_input = st.selectbox('Enter Paper Name prompt',['1','2'])
style_input = st.selectbox('Enter Explanation Style',['1','2'])
length_input = st.selectbox('Enter Length',['1','2'])

if st.button('Submit'):
 
    st.write("hello")