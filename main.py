from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    name: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/hello/{user_id}")
async def say_hello(user_id: int, user: User):
    return {
        "message": f"Hello {user.name}",
        "id": user.id,
        "name": user.name,
        "user_id": user_id
    }
