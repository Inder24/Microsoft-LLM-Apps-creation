from openai import OpenAI
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

# configure OpenAI service client 
client = OpenAI()

#deployment=os.environ['OPENAI_DEPLOYMENT']
deployment="gpt-3.5-turbo"

# add your completion code
prompt = "Complete the following: Once upon a time there was a girl who lived on a spaceship. She was very happy until one day she found out that she was not alone. She was very unhappy "
messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)

# print response
print(completion.choices[0].message.content)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.
