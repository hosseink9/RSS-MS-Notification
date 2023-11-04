from fastapi import HTTPException, status
from fastapi.routing import APIRouter

from app.schema.schemas import Otp, UserRequest
from ....utils.utils import create_otp, verify_otp

router = APIRouter(tags=["notification"])


