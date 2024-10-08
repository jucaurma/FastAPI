from fastapi import FastAPI, HTTPException, Body, Form
from typing import Union, Optional, Annotated
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
async def hello_world():
    return{"message": "Hello World!"}


#Ruta para saludo personalizado
@app.get("/saludo/{nombre}")
async def saludo_personalizado(nombre:str):
    return {"message": f"¡Hola, {nombre}!"}


@app.get("/todo1")
async def get_all():
    return [
        {"id":1, "description": "Learn Python", "complete": True},
         {"id":2, "description": "Learn Fast API", "complete": False},
    ]


TODO_LIST = [
    {"id":1, "description": "Learn Python", "complete": True},
    {"id":2, "description": "Learn Fast API", "complete": False},
    {"id":3, "description": "Tarea 3", "complete": False},
]


class Todo(BaseModel):
    id: Optional[int] = None
    description: str = Field(min_length=5, max_length=500)
    complete: bool = Field(default=False)



@app.get("/todo2")
async def get_all(complete: Union[bool, None] = None):
    if complete is not None:
        filtered_todos = list(filter(lambda todo: todo["complete"] == complete, TODO_LIST))
        return filtered_todos
    return TODO_LIST


@app.get("/todo2/{todo_id}")
async def get_todo(todo_id: int):
    try:
        todo_data = next(todo for todo in TODO_LIST if todo["id"] == todo_id )
        return todo_data
    except:
        raise HTTPException(status_code=404, detail="TODO no found")
    

@app.post("/todo1")
async def create_todo(id: int = Body(), description: str = Body(), complete: bool = Body()):
    TODO_LIST.append({
        "id": id,
        "description": description,
        "complete": complete
    })
    return TODO_LIST


@app.post("/todo2", response_model=Todo, name="Create TODO",
          summary="Create a TODO element",
          description="Create a TODO lelement given an id, a description and a complete status",
          deprecated=False)
async def create_todo(data: Todo):
    TODO_LIST.append(data)
    return data


@app.post("/support")
async def create_support_ticcket(title: Annotated[str, Form()], message: Annotated[str, Form()]):
    return{"title": title, "message": message}

