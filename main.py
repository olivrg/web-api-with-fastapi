from typing import Optinal

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optinal[str] = None
    price: float
    tax: Optinal[float] = None


app = FastAPI()


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}


# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}
