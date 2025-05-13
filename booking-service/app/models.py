from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
from datetime import datetime

class Booking(Base):
    __tablename__ = "bookings"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    item = Column(String, nullable=False)  # np. sala A, pokój 3
    timestamp = Column(DateTime, default=datetime.utcnow)
