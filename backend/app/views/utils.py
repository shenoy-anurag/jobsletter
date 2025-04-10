from pydantic import BaseModel
from fastapi import APIRouter, status, Depends
from fastapi.responses import FileResponse

from app.core.db import CurrentUser, get_current_active_superuser
from app.models.users import UserPublic


router = APIRouter()


@router.get('/favicon.ico', include_in_schema=False)
async def favicon():
    favicon_path = 'files/favicon.ico'
    return FileResponse(favicon_path)


@router.get("/ping", status_code=status.HTTP_200_OK)
async def ping():
    return {"message": "pong"}


@router.get("/protected", status_code=status.HTTP_200_OK)
async def protected(current_user: CurrentUser):
    return {"message": "get_current_user", "user": UserPublic(**current_user.__dict__)}


@router.get("/super-protected", dependencies=[Depends(get_current_active_superuser)], status_code=status.HTTP_200_OK)
async def super_protected():
    return {"message": "get_current_active_superuser"}
