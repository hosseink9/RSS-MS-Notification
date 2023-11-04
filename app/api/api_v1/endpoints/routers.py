from fastapi import HTTPException, status
from fastapi.routing import APIRouter

from app.schema.schemas import Otp, UserRequest
from ....utils.utils import create_otp, verify_otp

router = APIRouter(tags=["notification"])


@router.post('/create_otp', status_code=status.HTTP_201_CREATED)
async def generate_otp(data: UserRequest):
    await create_otp(data.id)
    return f'otp was sent to {data.username}'


@router.post('/verify_otp', status_code=status.HTTP_200_OK)
async def verify(data: Otp):
    result = await verify_otp(data.otp)
    return result
