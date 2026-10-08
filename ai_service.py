# LLM Calling

from google import genai
from app.config import api_key


def ai_analysis(text):
    client = genai.Client(api_key=api_key)

    prompt = f"""
From the following resume, analyze and answer the questions.

Resume:
{text}

1. Analyze the resume.
2. Give me 3 weaknesses from my resume.
3. Give me 3 strengths from my resume.
4. How can I improve my resume?
5. Give a rating out of 5 stars.
6. ATS Score.
7. Return the response in Markdown format.
8. Match % (Job Description vs Resume).

Also keep these things in mind:
1. Don't use technical jargon.
2. Keep it simple and short.
3. Maximum 1 line for each point.
4. Format the answer for better visualization.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text