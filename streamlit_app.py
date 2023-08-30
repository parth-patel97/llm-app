import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

# Add a title and intro text
st.title('Medical Symptom Checker')
st.text('This is a web app to allow tell the medical condition and some remedies.')
