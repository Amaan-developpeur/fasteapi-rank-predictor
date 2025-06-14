# FastAPI Rank Prediction API

This project demonstrates a simple API built using **FastAPI** to predict a student's rank based on their scores in Maths, Logical Reasoning, and English.

It's designed as a quick showcase of FastAPI + ML model integration.

---
## Problem Statement

The system takes input scores for:
- **Maths** (0–75)
- **Logical Reasoning** (0–75)
- **English** (0–50)

Each student is evaluated out of 200 total marks. If the **total score is below 50**, the student is **automatically disqualified**. The remaining qualified students are ranked using a machine learning model trained on synthetic data.

---

## Features

- 🏁 **Rank Prediction**: Returns a predicted rank (1 being the best) based on input scores.
- ✅ **Disqualification Logic**: Handles cutoff automatically (total score < 50).
- 🛠️ **FastAPI Backend**: RESTful API interface for integration.
- 📦 **Pickled ML Model**: Scikit-learn regression pipeline with preprocessing.

---

## Model Details

- **Algorithm**: Gradient Boosting Regressor  
- **Preprocessing**: `StandardScaler` for numerical features  
- **Target Variable**: Rank (lower is better)  
- **Data**: Synthetic dataset with 5000 rows generated to simulate real scoring patterns.

---



## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- scikit-learn (for deserializing the model)
- pydantic

---

## Setup & Run

### Clone the repo

```bash
git clone https://github.com/Amaan-developpeur/fastapi-rank-predictor.git
cd fastapi-rank-predictor

```
## Install Dependencies

pip install -r requirements.txt


## Run the Fast API app
uvicorn main:app --reload
```
```
## Visit API DOCS:
Swagger UI: http://127.0.0.1:8000/docs
