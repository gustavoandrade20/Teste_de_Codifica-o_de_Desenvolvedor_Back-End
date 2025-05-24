from fastapi import APIRouter, HTTPException
from app.services.whatsapp_service import send_whatsapp_message

router = APIRouter(prefix="/whatsapp")

@router.post("/send")
def send_message(to: str, message: str):
    try:
        send_whatsapp_message(to, message)
        return {"msg": "Message sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
