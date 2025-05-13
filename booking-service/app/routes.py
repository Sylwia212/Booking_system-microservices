from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas, models
from .database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/bookings", tags=["bookings"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.BookingOut)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    db_booking = models.Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

@router.get("/", response_model=list[schemas.BookingOut])
def get_bookings(db: Session = Depends(get_db)):
    return db.query(models.Booking).all()
