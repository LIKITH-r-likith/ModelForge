from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    username: str = Field(min_length=3)
    email: EmailStr

class UserUpdate(BaseModel):
    username: str = Field(min_length=3)
    email: EmailStr
