from http.client import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional
import json

app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


class UserIn(BaseModel):
    fname: str
    lname: str
    zname: str
    
msg = {"Hello": "World!!"}

# @app.get("/items/{item_id}are
@app.post('/add', response_model=UserIn)
async def add_people(user: UserIn):
    return user

@app.get('/people', response_model=UserIn)
async def get_people(user: UserIn):
    return user

@app.get('/')
async def root(msg):
    if msg == None:
        raise HTTPException(status_code=400, detail="not found error")
    return msg

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
