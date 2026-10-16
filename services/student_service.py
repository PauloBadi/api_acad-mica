from fastapi import HTTPException
from sqlmodel import Session, select

from models.student import Student
from schemas.student import StudentCreate


def create_student(
    student_data: StudentCreate,
    session: Session
):

    # Convierte los datos validados en una entidad que puede persistirse.
    student = Student(
        name=student_data.name,
        email=student_data.email,
        semester=student_data.semester,
        active=student_data.active
    )

    session.add(student)
    # Confirma la inserción en SQLite.
    session.commit()
    # Recarga el estudiante para obtener el ID generado.
    session.refresh(student)

    return student


def list_students(session: Session):

    statement = select(Student)

    return session.exec(statement).all()


def get_student(
    student_id: int,
    session: Session
):

    # Busca por clave primaria; devuelve None si no existe.
    student = session.get(
        Student,
        student_id
    )

    # Recurso inexistente: HTTP 404.
    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student