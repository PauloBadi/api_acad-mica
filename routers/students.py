from fastapi import APIRouter, Depends
from sqlmodel import Session

from database.database import get_session
from schemas.student import StudentCreate, StudentResponse

from services.student_service import (
    create_student,
    list_students,
    get_student
)


# Agrupa las rutas bajo /students y la etiqueta Students en Swagger.
router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# POST /students: crea un estudiante y responde 201.
@router.post(
    "",
    response_model=StudentResponse,
    status_code=201
)
def create_student_endpoint(
    student: StudentCreate,
    session: Session = Depends(get_session)
):

    return create_student(
        student,
        session
    )


# GET /students: lista todos los estudiantes.
@router.get(
    "",
    response_model=list[StudentResponse]
)
def list_students_endpoint(
    session: Session = Depends(get_session)
):

    return list_students(session)


# GET /students/{student_id}: 422 si no es entero, 404 si no existe.
@router.get(
    "/{student_id}",
    response_model=StudentResponse
)
def get_student_endpoint(
    student_id: int,
    session: Session = Depends(get_session)
):

    return get_student(
        student_id,
        session
    )