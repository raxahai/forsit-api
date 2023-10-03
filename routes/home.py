from fastapi.responses import JSONResponse
from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter(tags=["root"])


@router.get("/")
def home(response: Response) -> str:
    response.set_cookie(key="raza-session", value="raza-boi")
    return JSONResponse("This is home page", headers=response.headers)
