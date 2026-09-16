# Proyecto FastAPI - Tareas

Pequeño proyecto de API REST usando **FastAPI**.

## Descripción
API simple para gestionar tareas (CRUD completo) sin base de datos.  
Los datos se guardan en memoria.

## Endpoints
- `GET /` → Mensaje de bienvenida
- `POST /tareas` → Crear tarea
- `GET /tareas` → Listar todas las tareas
- `GET /tareas/{id}` → Obtener una tarea
- `PUT /tareas/{id}` → Actualizar una tarea
- `DELETE /tareas/{id}` → Eliminar una tarea

## Cómo ejecutarlo

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
