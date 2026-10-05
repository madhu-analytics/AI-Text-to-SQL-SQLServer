import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
my_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=my_key)

st.title("DataGPT")

st.write("Welcome to the data assistant")

user_input = st.text_input("Ask your Question?")

if st.button("Submit"):
    response = client.responses.create(model='gpt-5.6-sol',
                                       input=user_input)
    result = response.output_text
    st.write(result)