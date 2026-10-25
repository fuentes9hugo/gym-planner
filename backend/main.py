from fastapi import FastAPI


tags_metadata = [
    {
        "name": "muscles",
        "description": "Muscles CRUD related actions"
    }
]

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

# GET entry /
@app.get("/")
def read_root():
    return {"Hello": "World"}


# GET entry /muscles
@app.get("/muscles", tags=["muscles"])
def read_muscles():
    return {"Object": "Muscles"}