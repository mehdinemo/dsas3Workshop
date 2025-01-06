import httpx
from dotenv import load_dotenv
from groq import Groq
from openai import OpenAI

# Load environment variables for API credentials
load_dotenv()

http_client = httpx.Client(proxy="socks5://127.0.0.1:8080")
groq_client = Groq(http_client=http_client)
# openai_client = OpenAI()
