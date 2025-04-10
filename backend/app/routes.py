from fastapi import APIRouter

from app.views import users
from app.views import utils


api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(utils.router)