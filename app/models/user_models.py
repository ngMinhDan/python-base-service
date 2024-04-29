from pydantic import EmailStr, Field
from typing import Optional, Dict
from datetime import datetime
from beanie import Document


class User(Document):
    id: Optional[str] = Field(alias="_id")
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    role: Optional[str] = None
    location: Optional[str] = None
    extra_data: Optional[Dict] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "johndoe@example.com",
                "full_name": "John Doe",
                "disabled": False,
                "role": "admin",
                "location": "USA",
                 "extra_data": {
                    "feature_x": "value",
                    "feature_y": 123,
                },
                "created_at": "2021-08-01T00:00:00",
                "updated_at": "2021-08-01T00:00:00",
            }
        }