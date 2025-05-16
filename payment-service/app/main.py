from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class PaymentRequest(BaseModel):
    user_id: int
    amount: float

@app.post("/pay")
def process_payment(request: PaymentRequest):
    # Tu możesz zintegrować prawdziwą płatność np. Stripe
    if request.amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid amount")
    return {"status": "success", "message": f"Payment of {request.amount} confirmed for user {request.user_id}"}
