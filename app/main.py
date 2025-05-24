from fastapi import FastAPI
from app.api.routers import auth, clients, products, orders, whatsapp
from app.core.config import settings
import sentry_sdk

sentry_sdk.init(dsn=settings.SENTRY_DSN)

app = FastAPI(title="Lu Estilo API")

app.include_router(auth.router)
app.include_router(clients.router)
app.include_router(products.router)
app.include_router(orders.router)
app.include_router(whatsapp.router)
