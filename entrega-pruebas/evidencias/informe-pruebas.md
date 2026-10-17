# Informe de pruebas

- **Nombre:** _(Paulo Badillo)_
- **Herramienta:** Swagger (http://127.0.0.1:8000/docs)
- **Base de datos:** SQLite (`database.db`), iniciada vacía (se borró `database.db` antes de empezar)

**Cómo leerlo:**
- Los casos van en orden (P01, P02…). Ejecútalos en ese orden para que los IDs coincidan. Los IDs 999 deben no existir.
- Un 404 o 422 que era lo esperado es una prueba **APROBADA**.
- Cada evidencia es una captura en `evidencias/` con la petición y *Server response* (código y cuerpo). Una captura puede respaldar varios casos si lo anotas en la columna Evidencia.
- Para los nombres de 80 y 81 caracteres usa `python -c "print('A'*80)"` y `python -c "print('A'*81)"`.


## Listas vacías (ejecutar PRIMERO, con la base vacía)

| Caso | Endpoint | Datos enviados | Resultado esperado | Resultado obtenido | Estado | Evidencia |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | `GET /courses` | — | 200 y `[]` | | | `evidencias/P01.png` |
| P02 | `GET /students` | — | 200 y `[]` | | | `evidencias/P02.png` |

## Courses: POST

| Caso | Endpoint | Datos enviados | Resultado esperado | Resultado obtenido | Estado | Evidencia |
| --- | --- | --- | --- | --- | --- | --- |
| P03 | `POST /courses` | `{"name":"Desarrollo Web II","credits":3,"active":true}` | 201, ID 1 | | | `evidencias/P03.png` |
| P04 | `POST /courses` | `{"name":"Redes","credits":3}` | 201, ID 2, active true por defecto | | | `evidencias/P04.png` |
| P05 | `POST /courses` | `{"name":"Bases de Datos","credits":4,"active":false}` | 201, ID 3, active false | | | `evidencias/P05.png` |
| P06 | `POST /courses` | `{"name":"Cal","credits":3}` | 201, ID 4 (nombre de 3 caracteres) | | | `evidencias/P06.png` |
| P07 | `POST /courses` | `{"name":"<80 caracteres>","credits":3}` | 201, ID 5 (nombre de 80 caracteres) | | | `evidencias/P07.png` |
| P08 | `POST /courses` | `{"name":"Ética","credits":1}` | 201, ID 6 (créditos 1) | | | `evidencias/P08.png` |
| P09 | `POST /courses` | `{"name":"Proyecto Final","credits":6}` | 201, ID 7 (créditos 6) | | | `evidencias/P09.png` |
| P10 | `POST /courses` | `{"name":"ab","credits":3}` | 422 (nombre de 2 caracteres) | | | `evidencias/P10.png` |
| P11 | `POST /courses` | `{"name":"<81 caracteres>","credits":3}` | 422 (nombre de 81 caracteres) | | | `evidencias/P11.png` |
| P12 | `POST /courses` | `{"name":"Álgebra","credits":0}` | 422 (créditos 0) | | | `evidencias/P12.png` |
| P13 | `POST /courses` | `{"name":"Álgebra","credits":7}` | 422 (créditos 7) | | | `evidencias/P13.png` |
| P14 | `POST /courses` | `{"credits":3}` | 422 (falta name) | | | `evidencias/P14.png` |
| P15 | `POST /courses` | `{"name":"Álgebra"}` | 422 (falta credits) | | | `evidencias/P15.png` |
| P16 | `POST /courses` | `{"name":"Álgebra","credits":"abc"}` | 422 (credits no es entero) | | | `evidencias/P16.png` |
| P17 | `POST /courses` | `{"name":"Álgebra","credits":3,"active":"invalido"}` | 422 (active no es booleano) | | | `evidencias/P17.png` |

## Courses: GET

| Caso | Endpoint | Datos enviados | Resultado esperado | Resultado obtenido | Estado | Evidencia |
| --- | --- | --- | --- | --- | --- | --- |
| P18 | `GET /courses` | — | 200, lista de 7 cursos (activos e inactivos); los 422 anteriores no crearon nada | | | `evidencias/P18.png` |
| P19 | `GET /courses/1` | — | 200, curso 1 | | | `evidencias/P19.png` |
| P20 | `GET /courses/999` | — | 404 Course not found | | | `evidencias/P20.png` |
| P21 | `GET /courses/abc` | — | 422 | | | `evidencias/P21.png` |

## Courses: PUT

| Caso | Endpoint | Datos enviados | Resultado esperado | Resultado obtenido | Estado | Evidencia |
| --- | --- | --- | --- | --- | --- | --- |
| P22 | `PUT /courses/1` | `{"name":"Programación II","credits":4,"active":false}` | 200, mismo id 1, active false | | | `evidencias/P22.png` |
| P23 | `GET /courses` | — | 200, siguen 7 cursos (no aumenta) | | | `evidencias/P23.png` |
| P24 | `PUT /courses/4` | `{"name":"Cal","credits":3,"active":true}` | 200 (nombre de 3 caracteres) | | | `evidencias/P24.png` |
| P25 | `PUT /courses/5` | `{"name":"<80 caracteres>","credits":3,"active":true}` | 200 (nombre de 80 caracteres) | | | `evidencias/P25.png` |
| P26 | `PUT /courses/6` | `{"name":"Ética","credits":1,"active":true}` | 200 (créditos 1) | | | `evidencias/P26.png` |
| P27 | `PUT /courses/7` | `{"name":"Proyecto Final","credits":6,"active":true}` | 200 (créditos 6) | | | `evidencias/P27.png` |
| P28 | `PUT /courses/1` | `{"name":"ab","credits":4,"active":true}` | 422 (nombre de 2 caracteres) | | | `evidencias/P28.png` |
| P29 | `PUT /courses/1` | `{"name":"<81 caracteres>","credits":4,"active":true}` | 422 (nombre de 81 caracteres) | | | `evidencias/P29.png` |
| P30 | `PUT /courses/1` | `{"name":"Programación II","credits":0,"active":true}` | 422 (créditos 0) | | | `evidencias/P30.png` |
| P31 | `PUT /courses/1` | `{"name":"Programación II","credits":7,"active":true}` | 422 (créditos 7) | | | `evidencias/P31.png` |
| P32 | `PUT /courses/1` | `{"credits":4,"active":true}` | 422 (falta name) | | | `evidencias/P32.png` |
| P33 | `PUT /courses/1` | `{"name":"Programación II","active":true}` | 422 (falta credits) | | | `evidencias/P33.png` |
| P34 | `PUT /courses/1` | `{"name":"Programación II","credits":4}` | 422 (falta active) | | | `evidencias/P34.png` |
| P35 | `PUT /courses/1` | `{"name":"Programación II","credits":"abc","active":true}` | 422 (credits no es entero) | | | `evidencias/P35.png` |
| P36 | `PUT /courses/1` | `{"name":"Programación II","credits":4,"active":"invalido"}` | 422 (active no es booleano) | | | `evidencias/P36.png` |
| P37 | `PUT /courses/999` | `{"name":"Curso Fantasma","credits":3,"active":true}` | 404 | | | `evidencias/P37.png` |
| P38 | `PUT /courses/abc` | `{"name":"Curso Fantasma","credits":3,"active":true}` | 422 | | | `evidencias/P38.png` |
| P39 | `GET /courses/1` | — | 200, conserva los valores del primer PUT (los 422 no cambiaron nada) | | | `evidencias/P39.png` |

## Courses: DELETE (se elimina el curso 7)

| Caso | Endpoint | Datos enviados | Resultado esperado | Resultado obtenido | Estado | Evidencia |
| --- | --- | --- | --- | --- | --- | --- |
| P40 | `DELETE /courses/7` | — | 200 y {"message": "Course deleted"} | | | `evidencias/P40.png` |
| P41 | `GET /courses/7` | — | 404 | | | `evidencias/P41.png` |
| P42 | `GET /courses` | — | 200, la lista ya no tiene el ID 7 y los cursos 1 a 6 siguen | | | `evidencias/P42.png` |
| P43 | `DELETE /courses/7 (otra vez)` | — | 404 | | | `evidencias/P43.png` |
| P44 | `DELETE /courses/999` | — | 404 | | | `evidencias/P44.png` |
| P45 | `DELETE /courses/abc` | — | 422 | | | `evidencias/P45.png` |

## Students: POST y GET

| Caso | Endpoint | Datos enviados | Resultado esperado | Resultado obtenido | Estado | Evidencia |
| --- | --- | --- | --- | --- | --- | --- |
| P46 | `POST /students` | `{"name":"Ana Pérez","email":"ana@universidad.edu","semester":4}` | 201, ID 1, active true por defecto | | | `evidencias/P46.png` |
| P47 | `POST /students` | `{"name":"Luis Gómez","email":"luis@universidad.edu","semester":2,"active":false}` | 201, ID 2, active false | | | `evidencias/P47.png` |
| P48 | `POST /students` | `{"name":"Eva","email":"eva@universidad.edu","semester":3}` | 201, ID 3 (nombre de 3 caracteres) | | | `evidencias/P48.png` |
| P49 | `POST /students` | `{"name":"<80 caracteres>","email":"largo@universidad.edu","semester":3}` | 201, ID 4 (nombre de 80 caracteres) | | | `evidencias/P49.png` |
| P50 | `POST /students` | `{"name":"Carlos Soto","email":"carlos@universidad.edu","semester":1}` | 201, ID 5 (semestre 1) | | | `evidencias/P50.png` |
| P51 | `POST /students` | `{"name":"Laura Mejía","email":"laura@universidad.edu","semester":10}` | 201, ID 6 (semestre 10) | | | `evidencias/P51.png` |
| P52 | `POST /students` | `{"name":"Al","email":"al@universidad.edu","semester":3}` | 422 (nombre de 2 caracteres) | | | `evidencias/P52.png` |
| P53 | `POST /students` | `{"name":"<81 caracteres>","email":"x@universidad.edu","semester":3}` | 422 (nombre de 81 caracteres) | | | `evidencias/P53.png` |
| P54 | `POST /students` | `{"name":"Pedro Díaz","email":"p@universidad.edu","semester":0}` | 422 (semestre 0) | | | `evidencias/P54.png` |
| P55 | `POST /students` | `{"name":"Pedro Díaz","email":"p@universidad.edu","semester":11}` | 422 (semestre 11) | | | `evidencias/P55.png` |
| P56 | `POST /students` | `{"name":"Pedro Díaz","email":"","semester":3}` | 422 (email vacío) | | | `evidencias/P56.png` |
| P57 | `POST /students` | `{"name":"Pedro Díaz","semester":3}` | 422 (falta email) | | | `evidencias/P57.png` |
| P58 | `POST /students` | `{"email":"p@universidad.edu","semester":3}` | 422 (falta name) | | | `evidencias/P58.png` |
| P59 | `POST /students` | `{"name":"Pedro Díaz","email":"p@universidad.edu"}` | 422 (falta semester) | | | `evidencias/P59.png` |
| P60 | `POST /students` | `{"name":"Pedro Díaz","email":"p@universidad.edu","semester":"abc"}` | 422 (semester no es entero) | | | `evidencias/P60.png` |
| P61 | `POST /students` | `{"name":"Pedro Díaz","email":"p@universidad.edu","semester":3,"active":"invalido"}` | 422 (active no es booleano) | | | `evidencias/P61.png` |
| P62 | `GET /students` | — | 200, lista de 6 estudiantes (activos e inactivos); los 422 no crearon nada | | | `evidencias/P62.png` |
| P63 | `GET /students/1` | — | 200, estudiante 1 | | | `evidencias/P63.png` |
| P64 | `GET /students/999` | — | 404 Student not found | | | `evidencias/P64.png` |
| P65 | `GET /students/abc` | — | 422 | | | `evidencias/P65.png` |

## Persistencia e integración

| Caso | Endpoint | Datos enviados | Resultado esperado | Resultado obtenido | Estado | Evidencia |
| --- | --- | --- | --- | --- | --- | --- |
| P66 | Swagger /docs | — | Se ven las 5 rutas de Courses y las 3 de Students | | | `evidencias/P66.png` |
| P67 | GET /courses tras reiniciar Uvicorn | — | 200, cursos 1 a 6 y los cambios del PUT siguen | | | `evidencias/P67.png` |
| P68 | GET /courses/7 tras reiniciar | — | 404 (el curso eliminado sigue ausente) | | | `evidencias/P68.png` |
| P69 | GET /students tras reiniciar | — | 200, los 6 estudiantes siguen guardados | | | `evidencias/P69.png` |
| P70 | POST /courses y luego GET /students | un curso válido | La lista de estudiantes no cambia (cursos y estudiantes son independientes) | | | `evidencias/P70.png` |

Total de casos: 70. Estado de cada caso: APROBADO o FALLIDO.
