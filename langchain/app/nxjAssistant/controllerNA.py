from fastapi import APIRouter, HTTPException
from app.nxjAssistant.serviceNA import process_ask
from pydantic import BaseModel

router = APIRouter(
    prefix="/na",
    tags=["na"],
    responses={404: {"description": "Not found"}},
)

class InputModel(BaseModel):
    user_input: str

@router.post("/query")
def handle_ask(input: InputModel):
    try:
        response = process_ask(input.user_input)
        return {"success": True, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
