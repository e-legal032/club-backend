# app/core/config.py
from pydantic import BaseModel

class Settings(BaseModel):
    app_name: str = "Club de Fútbol API"

settings = Settings()
