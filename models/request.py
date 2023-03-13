from pydantic import BaseModel


class Request(BaseModel):
    load: float
    fuels: dict
    powerplants: list
