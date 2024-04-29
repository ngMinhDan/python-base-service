from fastapi import APIRouter

router = APIRouter()

@router.get("/admin")
async def get():
    return {"status": "admin"}