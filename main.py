from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello_world():
    return{"message": "Hello World!"}


#Ruta para saludo personalizado
@app.get("/saludo/{nombre}")
async def saludo_personalizado(nombre:str):
    return {"message": f"¡Hola, {nombre}!"}
