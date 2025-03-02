from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()
PRODUCTS = []

class Product(BaseModel):
    id: int
    name:str
    price:int

@app.get("/", response_model=list[Product])
def get_products():
    return PRODUCTS

@app.post("/", response_model=Product)
def create_products(data: Product):
    PRODUCTS.apend(data)
    return data

@app.get("/{id}")
def get_product_by_id(id:int):
    pass

@app.put("/{id}")
def update_product(id:int):
    pass

@app.delete("/{id}")
def delete_product(id:int):
    pass