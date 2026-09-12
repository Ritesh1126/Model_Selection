import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Key Not Found plz try again")
