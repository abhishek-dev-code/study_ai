from fastapi import FastAPI
from pydantic import BaseModel
from models.study_assistant import StudyAssistant
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

app = FastAPI()
assistant = StudyAssistant()

class Query(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "Study Assistant is running successfully!"}

@app.post("/ask")
def ask_question(data: Query):
    answer = assistant.get_answer(data.query)
    return {"answer": answer}
