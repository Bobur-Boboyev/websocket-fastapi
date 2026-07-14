from pydantic import BaseModel


class Order(BaseModel):
    food: str
    count: int