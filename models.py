
from sqlalchemy import Column, String, Table
from app.database import metadata, engine
from app.schemas import FormData

form_table = Table(
    "udyam_form",
    metadata,
    Column("aadhaar", String, primary_key=True),
    Column("pan", String),
    Column("pincode", String),
    Column("state", String),
    Column("city", String),
)

def create_tables():
    metadata.create_all(engine)

def save_form_data(data: FormData):
    query = form_table.insert().values(
        aadhaar=data.aadhaar,
        pan=data.pan,
        pincode=data.pincode,
        state=data.state,
        city=data.city
    )
    with engine.connect() as conn:
        conn.execute(query)
