from datetime import timedelta, datetime
from fastapi import HTTPException, status
import random

from ..db.db import RedisDB


async def create_otp(id: str):
    otp = str(random.randint(1000, 9999))
    otp_expire = (
        datetime.utcnow() + timedelta(minutes=1)).strftime("%d/%m/%Y, %H:%M:%S")
    redis = RedisDB()
    await redis.set_data(key=otp, value=id, ex=100)
    print(f"generated:{otp}  until:{otp_expire}")

