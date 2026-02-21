from fastapi import APIRouter

router = APIRouter(prefix = "/api/v1/test", tags = ["Test Routes"])

@router.get("/")
def hello(): 
    return {
        "message": "Hello From FastAPI Server Mini Router!"
    }