


import google.generativeai as genai
import os

genai.configure(api_key="Use Your own API ID")##use own API ID

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("what is programming")
print(response.text)