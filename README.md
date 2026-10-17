# API Académica

API hecha con **FastAPI, SQLModel y SQLite** para administrar cursos y estudiantes.

## Funcionalidades

- **Courses:** crear, listar, consultar, actualizar (PUT) y eliminar (DELETE).
- **Students:** crear, listar y consultar.
- Los datos se guardan en SQLite (`database.db`), con las tablas `course` y `student`.
- Validación de datos: errores `404` (no existe) y `422` (datos inválidos).

## Cómo ejecutarlo

Desde la carpeta que contiene `main.py`:

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1      # Windows (Linux/macOS: source venv/bin/activate)
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Abre http://127.0.0.1:8000/docs para probar los endpoints.

## Endpoints

| Método | Ruta | Descripción |
| --- | --- | --- |
| POST | `/courses` | Crear curso (201) |
| GET | `/courses` | Listar cursos |
| GET | `/courses/{course_id}` | Consultar curso |
| PUT | `/courses/{course_id}` | Actualizar curso (name, credits y active obligatorios) |
| DELETE | `/courses/{course_id}` | Eliminar curso |
| POST | `/students` | Crear estudiante (201) |
| GET | `/students` | Listar estudiantes |
| GET | `/students/{student_id}` | Consultar estudiante |

## Reglas de validación

- **Curso:** `name` de 3 a 80 caracteres, `credits` entre 1 y 6, `active` booleano (en POST es opcional y vale `true`; en PUT es obligatorio).
- **Estudiante:** `name` de 3 a 80 caracteres, `email` no vacío, `semester` entre 1 y 10, `active` opcional (`true` por defecto).

## Estructura

```text
api_acad-mica/
├── main.py                  # Crea la app y registra los routers
├── database/database.py     # Conexión a SQLite y sesiones
├── models/                  # Tablas: course.py, student.py
├── schemas/                 # Validación: course.py, student.py
├── services/                # Lógica de datos: course_service.py, student_service.py
├── routers/                 # Endpoints: courses.py, students.py
├── entrega-pruebas/         # Informe y evidencias de pruebas
└── requirements.txt
```

Flujo de una petición: **Router → Schema → Service → Model/Session → SQLite**.
