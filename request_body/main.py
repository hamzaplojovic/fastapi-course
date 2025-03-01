from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
PRODUCTS = []

class Product(BaseModel):
    id: int
    name: str
    price: int


@app.get("/", response_model=list[Product])
def get_products():
    return PRODUCTS

@app.post("/", response_model=Product)
def create_product(data:Product):
    PRODUCTS.append(data)
    return data