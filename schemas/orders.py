from uuid import UUID, uuid4
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Order(BaseModel):
    id: UUID = uuid4()
    price: float
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    deleted_at: Optional[datetime] = None
