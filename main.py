from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Mi API de Tareas",
    description="Proyecto pequeño con FastAPI para la tarea",
    version="1.0.0"
)

# Lista en memoria (sin base de datos)
tareas = []
contador_id = 0

class Tarea(BaseModel):
    texto: str
    hecha: bool = False

class TareaRespuesta(BaseModel):
    id: int
    texto: str
    hecha: bool

@app.get("/")
def inicio():
    return {
        "mensaje": "¡Bienvenido a mi API de Tareas con FastAPI!",
        "documentacion": "/docs"
    }

@app.post("/tareas", response_model=TareaRespuesta)
def crear_tarea(tarea: Tarea):
    global contador_id
    nueva_tarea = {
        "id": contador_id,
        "texto": tarea.texto,
        "hecha": tarea.hecha
    }
    tareas.append(nueva_tarea)
    contador_id += 1
    return nueva_tarea

@app.get("/tareas", response_model=List[TareaRespuesta])
def listar_tareas():
    return tareas

@app.get("/tareas/{tarea_id}", response_model=TareaRespuesta)
def obtener_tarea(tarea_id: int):
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.put("/tareas/{tarea_id}", response_model=TareaRespuesta)
def actualizar_tarea(tarea_id: int, tarea_actualizada: Tarea):
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            tarea["texto"] = tarea_actualizada.texto
            tarea["hecha"] = tarea_actualizada.hecha
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.delete("/tareas/{tarea_id}")
def eliminar_tarea(tarea_id: int):
    for i, tarea in enumerate(tareas):
        if tarea["id"] == tarea_id:
            tareas.pop(i)
            return {"mensaje": f"Tarea {tarea_id} eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
