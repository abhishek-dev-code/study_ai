from google import genai
import os

class StudyAssistant:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables.")

        self.client = genai.Client(api_key=api_key)
        self.model = "models/gemini-2.5-flash"   # <-- CORRECT MODEL NAME

    def get_answer(self, query: str):
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=query
            )
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"
