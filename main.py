from fastapi import FastAPI
from routers import todo, support
from enum import Enum

class Tags(Enum):
    home: str = "Home"

app = FastAPI(
    tittle="TODO API",
)

app.include_router(todo.router)
app.include_router(support.router)


@app.get("/", tags=[Tags.home])
async def home():
    return {
        "name": "TODO Rest API",
        "version": "1.0.0"
    }