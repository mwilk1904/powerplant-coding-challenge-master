from fastapi import FastAPI
from models.request import Request
from power_dispatcher import get_power_dispatch

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Powerplant Coding Challenge"}


@app.post('/productionplan')
def power_dispatcher(data: Request):
    return get_power_dispatch(data)
