📘 Study Assistant AI

A lightweight personal study companion built with FastAPI + Google Gemini API

🚀 Overview

Study Assistant AI is a minimal, production-ready study helper built in Python.
It answers questions, plans study tasks, and maintains a small personalized learning memory.

Project goals:

Clean backend design

Lightweight and fast

Modular agents

Real deployable architecture (Docker + Cloud Run)

🧠 Features

✔ Doubt solving (concept explanations)
✔ Study planning assistant
✔ Resource finder (articles, videos, references)
✔ Memory-powered personalization
✔ API endpoint for frontend integration
✔ Google Gemini 2.5 Flash model support
✔ Docker + Cloud Run deployable

🏗 Tech Stack

Python 3.10+
FastAPI
Google Gemini (Generative AI)
Uvicorn
Docker
Cloud Run (optional deploy)

📂 Project Structure
study_ai/
├── main.py
├── .env
├── README.md
├── requirements.txt
├── LICENSE
│
├── models/
│   └── study_assistant.py
│
├── agents/
│   ├── doubt_solver.py
│   ├── resource_finder.py
│   └── study_planner.py
│
├── tools/
│   └── search_tool.py
│
├── memory/
│   ├── user_profile.json
│   └── __init__.py
│
├── user_profile/
│   ├── history.json
│   └── history.py
│
└── deployment/
    ├── Dockerfile
    └── cloudrun.yaml

📡 API Endpoints
✓ Status Check

GET /

{ 
  "message": "Study Assistant is running successfully!" 
}

✓ Ask a question

POST /ask
Request:

{ "query": "What is Newton's second law?" }


Response:

{
  "answer": "Force equals mass times acceleration..."
}

🔑 Setup Instructions

1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Set your Google Gemini API Key
.env file create kare:

GOOGLE_API_KEY=your_key_here

(.env.example already provided)

3️⃣ Run locally
python -m uvicorn main:app --reload

🐳 Docker Support
Build
docker build -t study-assistant .

Run
docker run -p 8000:8000 study-assistant

☁ Deploy on Cloud Run
gcloud run deploy study-assistant \
  --source . \
  --region asia-south1 \
  --platform managed \
  --allow-unauthenticated

🔍 Why this project?

I built this project to explore:

How LLMs can be integrated into real backend services

Practical prompt engineering

Agent-based modular design

Deploying lightweight AI assistants in the cloud

It works well as:

A personal assistant

A starter template for AI agents

A base for larger study applications

📜 License

MIT License

🙌 Acknowledgements

Google Gemini API

FastAPI community