# 🎯 FastAPI Rank Prediction API

This project demonstrates a simple API built using **FastAPI** to predict a student's rank based on their scores in Maths, Logical Reasoning, and English.

It's designed as a quick showcase of FastAPI + ML model integration.

---

## 🚀 Features

- FastAPI-powered REST endpoint
- Input validation using Pydantic
- Model inference using a pre-trained pickle model (`rank_model.pkl`)
- Simple logic to disqualify students below a total score threshold

---

## 📦 Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- scikit-learn (for deserializing the model)
- pydantic

---

## 🔧 Setup & Run

### 1️⃣ Clone the repo

```bash
git clone https://github.com/Amaan-developpeur/fastapi-rank-predictor.git
cd fastapi-rank-predictor
