import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

try:
    user_prompt = sys.argv[1]
except IndexError as e:
    print("Error: No Prompt Given")
    sys.exit(1)

try:
    user_flag = sys.argv[2]
except IndexError as e:
    user_flag = "Empty"


messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

response = client.models.generate_content(
    model="gemini-2.0-flash-001", contents=messages
)

print(response.text)

if user_flag == "--Verbose":
    print(f"User Prompt: {user_prompt}")
    print(f"Prompt Tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response Tokens: {response.usage_metadata.candidates_token_count}")
