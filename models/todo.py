from pydantic import BaseModel
from typing import Optional,Annotated

from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class Todo(BaseModel):
    id: Optional[UUID] = None
    title: str
    action: str

    class Config:
        json_encoders = {
            UUID: lambda v: str(v)
        }


