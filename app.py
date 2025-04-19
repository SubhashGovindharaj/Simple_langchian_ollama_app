from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama  # ✅ FIXED: use class, not module
import streamlit as st
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Set LangSmith-related env variables
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ('system', "You're a helpful assistant. Please respond to the questions asked!"),
    ('user', 'Question: {question}')
])

# Streamlit UI
st.title('Langchain demo with LLaMA3')
input_text = st.text_input('What question do you have in mind?')

# ✅ Corrected Ollama call
llm = Ollama(model='llama3')
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))