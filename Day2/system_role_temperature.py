import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Key Not Found plz try again")

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    temperature = 0.2,
    messages=[
        {"role":"system","content":"You are helpful assistant"},
        {"role":"user","content":"Write Roman in two sentence"}
    ]
)

print(response.choices[0].message.content)
