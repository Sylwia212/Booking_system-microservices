from pydantic import BaseModel
from datetime import datetime

class BookingCreate(BaseModel):
    username: str
    item: str

class BookingOut(BaseModel):
    id: int
    username: str
    item: str
    timestamp: datetime

    class Config:
        orm_mode = True
