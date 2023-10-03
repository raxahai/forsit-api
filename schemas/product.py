from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from datetime import datetime


class Product(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    description: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    deleted_at: Optional[datetime] = None
