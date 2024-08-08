""" first fastapi tutorial """
from enum import Enum

from fastapi import FastAPI


class MLModels(str, Enum):
    nul = "alexnet"
    een = "resnet"
    twee = "lenet"


app = FastAPI()
fake_db = [
    {"een": "ween"},
    {"un": 1},
    {"twee": 2},
    {"deux": "farkus"},
    {"drie": "vorst"},
]


@app.get("/")
async def get0():
    return {"message": "Bienvenue à api vite"}


@app.get("/{item}")
async def get1(item):
    return {"item": item}


@app.get("/id/{item_id}")
async def get2(item_id: int):
    return {"item id": item_id}


@app.get("/naam/{item_naam}")
async def get3(item_naam: str):
    return {"item naam": item_naam}


@app.get("/mlmodels/{name}")
async def get_mlmodel(name: MLModels):
    message = "residual"
    if name is MLModels.nul:
        message = "Deep"
    elif name.value == "lenet":
        message = "LeCNN"

    return {"mlmodel": name, "message": message}


@app.get("/uploads/{file_path:path}")
async def upload(file_path: str):
    if file_path.endswith("pdf"):
        return {"uploaded_to": file_path}
    return {"invalid_path": file_path}


@app.get("/fakedb/")
async def fakedb(skip: int = 0, limit: int = 10):
    return fake_db[skip: skip + limit]
