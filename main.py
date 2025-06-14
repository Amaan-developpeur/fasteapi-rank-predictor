import pickle

with open('rank_model.pkl', 'rb') as fp:
    model = pickle.load(fp)

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Rank Prediction API")

# Input schema
class ScoreInput(BaseModel):
    maths: int = Field(..., ge=0, le=75)
    reasoning: int = Field(..., ge=0, le=75)
    english: int = Field(..., ge=0, le=50)

@app.post("/predict-rank/")
def predict_rank(scores: ScoreInput):
    total = scores.maths + scores.reasoning + scores.english

    if total < 50:
        return {"status": "Disqualified", "total_score": total}

    # Prepare data for model prediction
    input_data = [[scores.maths, scores.reasoning, scores.english]]
    predicted_rank = model.predict(input_data)[0]

    return {
        "status": "Qualified",
        "predicted_rank": int(predicted_rank),
        "total_score": total
    }
