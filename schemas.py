
from pydantic import BaseModel

class FormData(BaseModel):
    aadhaar: str
    pan: str
    pincode: str = ""
    state: str = ""
    city: str = ""
