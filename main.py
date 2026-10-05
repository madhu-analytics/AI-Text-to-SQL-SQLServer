#we want to send a sql request to openai

from openai import OpenAI
from dotenv import load_dotenv
import os
from mydb import execute_query,get_schema

load_dotenv()

my_key = os.getenv('OPENAI_API_KEY')
#print(my_key)
schema = get_schema('orders')

userinput = input('Ask your question: ')
final_prompt = f'''Generate a SQL query for the below schema {schema},
question : {userinput}
just give sql only
'''

client = OpenAI(api_key=my_key)
response = client.responses.create(model='gpt-5.6-sol',
                        input=final_prompt)

query = response.output_text
result = execute_query(query)
print(query)
print(result)