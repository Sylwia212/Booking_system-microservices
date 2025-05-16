from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Notification(BaseModel):
    user_id: int
    message: str

@app.post("/notify")
def send_notification(notification: Notification):
    # Tu możesz zintegrować np. SMTP lub usługę email API
    print(f"Sending notification to user {notification.user_id}: {notification.message}")
    return {"status": "sent", "to": notification.user_id}
