from typing import List
from schemas.product import Product
from fastapi import APIRouter
from datetime import datetime
from uuid import UUID

router = APIRouter(prefix='/api/v1/product', tags=["Products"])

db: List[Product] = [
    Product(name="Apple", description="This is a fruit",
            created_at=datetime.now(), updated_at=datetime.now())
]


@router.get('/all', status_code=200)
async def products() -> List[Product]:
    return db


@router.post('/', status_code=200)
async def create_product(product: Product) -> Product:
    db.append(product)
    return product


@router.delete('/{id}', status_code=200)
async def delete_product(id: UUID):
    for product in db:
        if product.id == id:
            product.deleted_at = datetime.now()
    return {"id": id}
