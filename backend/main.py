from fastapi import FastAPI
from docs import tags_metadata
from musclesdata import MusclesData


# Objeto para trabajar con los datos de prueba
muscles = MusclesData()

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

# Default
# GET /
@app.get("/")
def read_root():
    return {"Hello": "World"}


# Muscles
# GET /muscles
@app.get("/muscles", tags=["muscles"])
async def read_muscles():
    return await muscles.get_muscles()

# GET /muscles/{muscle_id}
@app.get("/muscles/{muscle_id}",tags=["muscles"])
async def read_muscle(muscle_id: int):
    return await muscles.get_muscle(muscle_id)