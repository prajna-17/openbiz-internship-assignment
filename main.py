
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import FormData
from app.models import create_tables, save_form_data
from app.database import engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_tables()

@app.post("/submit")
async def submit_form(data: FormData):
    if len(data.aadhaar) != 12 or not data.aadhaar.isdigit():
        raise HTTPException(status_code=400, detail="Invalid Aadhaar number.")
    if not data.pan.isalnum() or len(data.pan) != 10:
        raise HTTPException(status_code=400, detail="Invalid PAN format.")
    save_form_data(data)
    return {"message": "Form submitted successfully."}
