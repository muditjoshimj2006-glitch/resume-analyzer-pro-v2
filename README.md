# 📄 Resume Analyzer Pro V2

An AI-powered Resume Analyzer built with FastAPI and Google Gemini.

This project allows users to upload a PDF resume, extracts the text, and generates professional resume analysis using Google's Gemini API.

---

## 🚀 Features

- Upload PDF Resume
- Extract Text from PDF
- AI Resume Analysis
- ATS-style Feedback
- Resume Strengths
- Resume Weaknesses
- Improvement Suggestions

---

## 🛠 Tech Stack

- Python
- FastAPI
- Google Gemini API
- PyPDF
- Python Dotenv

---

## 📂 Project Structure

```
resume_analyzer_pro_v2/

│── app/
│   ├── routers/
│   ├── services/
│   ├── config.py
│
│── uploads/
│── .env
│── .gitignore
│── requirements.txt
│── main.py
│── README.md
```

---

## ⚙ Installation

Clone the repository

```bash
git clone <your-repository-url>
```

Move into project

```bash
cd resume_analyzer_pro_v2
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the server

```bash
uvicorn main:app --reload
```

---

## 📍API Endpoint

### Home

```
GET /
```

### Upload Resume

```
POST /upload
```

---

## 📌 Future Improvements

- Resume vs Job Description Matching
- ATS Score Improvement
- Multiple Resume Comparison
- Chat with Resume
- Resume Rewrite using AI

---

## 👨‍💻 Author

**Mudit Joshi**

Learning Project built while exploring:

- FastAPI
- Modular Project Architecture
- PDF Parsing
- Google Gemini API Integration
- Backend Development