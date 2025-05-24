from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SENTRY_DSN: str = ""
    DATABASE_URL: str = "postgresql://user:password@localhost/db"
    JWT_SECRET: str = "supersecret"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_MINUTES: int = 30
    TWILIO_ACCOUNT_SID: str = ""
    TWILIO_AUTH_TOKEN: str = ""
    TWILIO_PHONE_NUMBER: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
