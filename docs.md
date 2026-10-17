# Guía breve de la API Académica

## Qué hace cada capa

| Capa | Archivo | Función |
| --- | --- | --- |
| Router | `routers/` | Recibe la petición HTTP y llama al service. |
| Schema | `schemas/` | Valida los datos que entran y salen (Pydantic). |
| Service | `services/` | Contiene la lógica y usa la sesión de la base de datos. |
| Model | `models/` | Representa la tabla (`table=True`). |
| Session | `database/database.py` | Conexión con SQLite; `Depends(get_session)` la entrega a cada petición. |
| SQLite | `database.db` | Archivo donde se guardan los datos. |

## Conceptos clave

- `session.add()` agrega el objeto, `session.commit()` guarda el cambio de forma permanente y `session.refresh()` recarga el objeto (por ejemplo, para obtener el `id` generado).
- Los datos siguen existiendo al reiniciar Uvicorn porque están en el archivo `database.db`, no en memoria.
- `PUT` modifica el mismo registro (el `id` no cambia); `DELETE` usa `session.delete()` y `commit()`.
- **404:** el recurso no existe. **422:** los datos enviados no cumplen la validación (o el ID no es entero).
- Cursos y estudiantes usan el mismo `engine`, así que están en la misma base de datos, en tablas distintas.

## Recorrido de una petición

Cliente → Router → Schema (valida) → Service (lógica) → Model + Session → SQLite → respuesta JSON.

## Ejecución

Consulta el [README](README.md).
