from pydantic import BaseModel


class UserRequest(BaseModel):
    id: str
    username: str


class Otp(BaseModel):
    otp: str
