""" first fastapi tutorial """

from fastapi import FastAPI

app = FastAPI()


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
