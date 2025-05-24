from twilio.rest import Client
from app.core.config import settings

def send_whatsapp_message(to: str, message: str):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    client.messages.create(
        from_=settings.TWILIO_WHATSAPP_NUMBER,
        body=message,
        to=f'whatsapp:{to}'
    )
