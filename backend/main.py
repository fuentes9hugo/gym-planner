from fastapi import FastAPI, Response, status
from docs import tags_metadata
from routinedata import RoutineData


# Objeto para trabajar con los datos de prueba
routine = RoutineData()

# FastAPI object app
app = FastAPI(
    title="GymRoutinAPI",
    description="API RESTful for a complete gym routine management",
    version="0.0.2",
    contact={
        "name": "Hugo Fuentes",
        "url": "http://localhost:8000/",
    },
    license_info={
        "name": "GPLv3",
        "url": "https://gnu.org",
    },
    openapi_tags=tags_metadata
)


# APIRESTful configuration
# Endpoint definition

# DEFAULT
# GET /
@app.get("/")
def read_root():
    return {"Hello": "World"}


# MUSCLES
# GET /muscles
@app.get("/muscles", tags=["muscles"])
async def read_muscles(skip: int = 0, total: int = 10, all_muscles: bool | None = None):
    return await routine.get_muscles(skip, total, all_muscles)

# GET /muscles/{muscle_id}
@app.get("/muscles/{muscle_id}",tags=["muscles"], status_code=status.HTTP_200_OK)
async def read_muscle(muscle_id: int, response: Response):
    # Search muscle
    muscle = await routine.get_muscle(muscle_id)
    # If found, return muscle
    if muscle: return muscle
    # Else, return error 404
    response.status_code = status.HTTP_404_NOT_FOUND
    return {f"Error, {muscle_id} not found"}


# EXERCISES
# GET /exercises
@app.get("/exercises", tags=["exercises"])
async def read_exercises(skip: int = 0, total: int = 10, all_exercises: bool | None = None):
    return await routine.get_exercises(skip, total, all_exercises)

# GET /exercises/{exercise_id}
@app.get("/exercises/{exercise_id}",tags=["exercises"], status_code=status.HTTP_200_OK)
async def read_exercise(exercise_id: int, response: Response):
    # Search exercise
    exercise = await routine.get_exercise(exercise_id)
    # If found, return exercise
    if exercise: return exercise
    # Else, return error 404
    response.status_code = status.HTTP_404_NOT_FOUND
    return {f"Error, {exercise_id} not found"}

# GET /exercises/{exercise_id}/muscles/{muscle_id}
@app.get("/exercises/{exercise_id}/muscles/{muscle_id}",tags=["exercises"], status_code=status.HTTP_200_OK)
async def read_exercise_muscle(exercise_id: int, muscle_id: int, response: Response):
    # Search exercise
    muscle = await routine.get_muscle_exercise(exercise_id, muscle_id)
    # If found, return exercise
    if muscle: return muscle
    # Else, return error 404
    response.status_code = status.HTTP_404_NOT_FOUND
    return {f"Error, exercise: {exercise_id} or muscle: {muscle_id} not found"}