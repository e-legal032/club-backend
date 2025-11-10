# Club de Fútbol – Backend

Backend del sistema de gestión deportiva (FastAPI + SQLAlchemy + Alembic).

## Requisitos
- Python 3.12 (automático en GitHub Codespaces)
- Dependencias: ver `requirements.txt`

## Desarrollo
1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
2. Levantar servidor
   ```bash
   uvicorn app.main:app --reload --port 8000

## Endpoints de prueba
- Health check: http://localhost:8000/api/health

## Documentación automática
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Estructura
- `app/` → código fuente
  - `api/` → rutas y controladores
  - `models/` → modelos de base de datos
  - `schemas/` → validaciones y serialización (Pydantic)
  - `crud/` → operaciones de acceso a datos
  - `core/` → configuración y conexión a la base de datos
- `requirements.txt` → dependencias
- `.devcontainer/` → configuración para reproducibilidad
- `.gitignore` → archivos y carpetas ignorados por Git

## Notas de Codespaces
- Al levantar el servidor, Codespaces expone el puerto 8000 mediante “port forwarding”. Usá la URL pública que te muestre el panel de puertos para acceder a la API.
- Si ves “Cannot GET” en la raíz `/`, probá directamente `/api/health`.



