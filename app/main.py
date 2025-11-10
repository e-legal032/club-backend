# app/main.py
from fastapi import FastAPI
from .api.routes import router as api_router

# Inicializamos la aplicación FastAPI
app = FastAPI(
    title="Club de Fútbol API",
    version="0.1.0"
)

# Incluimos las rutas definidas en app/api/routes.py
app.include_router(api_router, prefix="/api")
