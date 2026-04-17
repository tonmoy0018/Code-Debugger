from google import genai
from dotenv import load_dotenv
import os , io

load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=my_api_key)

def issue_founder(image):
    prompt = "Find and explain the issue from the given image of the code in easy way and in short. Do not includ the fix or solution here. Use markdown language for better understanding"

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[image, prompt]
    )
    return response.text

def Hints_Only(image):
    prompt = "Explain the solution of the error code. Use markdoown languagse. Don't provide the fixed code, only provide where to fix the errors, what to fix and how to fix"

    response1 = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[image, prompt]
    )
    return response1.text

def Fixed_code(image):
    prompt = "Provide the corrected code of the error code and Explain the solution. Use markdoown languagse."

    response2 = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[image, prompt]
    )
    return response2.text
