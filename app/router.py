from fastapi import APIRouter

from app.schema import MessageInput, CompletionResponse
from app.services import generate_response
from scalar_fastapi import get_scalar_api_reference
from fastapi import FastAPI
router = APIRouter()
app = FastAPI()

@router.post("/completions", response_model=CompletionResponse)
def start_completion(body: MessageInput):
    response = generate_response(body.message)
    return CompletionResponse(response = response)

@router.get("/scalar")
def documentation():
    return get_scalar_api_reference(title=app.title, openapi_url=app.openapi_url)