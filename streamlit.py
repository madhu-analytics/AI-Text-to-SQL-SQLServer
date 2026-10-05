import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

from mydb import execute_query, get_schema

# Load environment variables
load_dotenv()

# OpenAI API key
my_key = os.getenv("OPENAI_API_KEY")

# OpenAI client
client = OpenAI(api_key=my_key)

# Get schema
schema = get_schema("orders")

# Streamlit UI
st.title("🤖 Text to SQL AI Assistant")
st.write("Ask a question about the orders table and get the SQL result.")

# User input
userinput = st.text_input(
    "Ask your question:",
    placeholder="Example: Show me the top 5 sales"
)

# Button
if st.button("Generate SQL"):

    if userinput:

        # Prompt
        final_prompt = f"""
        Generate a SQL query for the below schema:

        {schema}

        Question:
        {userinput}

        Just give SQL only.
        """

        # Call OpenAI
        response = client.responses.create(
            model="gpt-5.6-sol",
            input=final_prompt
        )

        # Get generated SQL
        query = response.output_text.strip()

        # Display SQL
        st.subheader("Generated SQL")
        st.code(query, language="sql")

        # Execute SQL
        try:
            result = execute_query(query)

            st.subheader("Query Result")
            st.dataframe(result)

        except Exception as e:
            st.error(f"Error executing query: {e}")

    else:
        st.warning("Please enter a question.")