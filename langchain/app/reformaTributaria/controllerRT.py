from fastapi import APIRouter, HTTPException
from app.reformaTributaria.servicesRT import process_user_query
from pydantic import BaseModel

router = APIRouter(
    prefix="/rt",
    tags=["rt"],
    responses={404: {"description": "Not found"}},
)

class InputModel(BaseModel):
    user_input: str

@router.post("/query")
def handle_query(input: InputModel):
    try:
        response = process_user_query(input.dict())
        return {"success": True, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
