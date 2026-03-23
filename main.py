from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

from database import SessionLocal, engine, Base
import models
import schemas
import services
import datetime

now = datetime.datetime.now()

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Payments Intake API",
    version="1.0"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/payments", response_model=schemas.PaymentResponse)

#@app.post("/payments", data=data)
def create_payment(payment: schemas.PaymentRequest, db: Session = Depends(get_db)):

    if payment.amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid amount")
    print("Transaction completed at: ", now)
    transaction = services.create_payment(db, payment)
    return {
        "transaction_id": str(transaction.id),
        "status": transaction.status
    }