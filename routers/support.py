from fastapi import Form, APIRouter
from typing import Annotated

router = APIRouter(
    prefix="/support",
    tags=["Support"]
)

@router.post("/support")
async def create_support_ticket(
    title: Annotated[str, Form()], 
    message: Annotated[str, Form()]
):
    return{"title": title, "message": message}