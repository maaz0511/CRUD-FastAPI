from pydantic import BaseModel, Field, StrictInt, StrictStr, EmailStr
from typing import Optional

class Student(BaseModel):
    std_id: StrictInt = Field(..., gt=0, title="Student ID")
    std_name: StrictStr = Field(..., min_length=5, max_length=30, title="Student Name")
    std_age: StrictInt = Field(..., gt=3, title="Student Age")
    std_email: EmailStr = Field(..., title="Student Email")