from fastapi import FastAPI
from pydantic import BaseModel

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

@app.get("/{id}", response_model=Product)
def get_product_by_id(id:int):
    for product in PRODUCTS:
        if product["id"] == id:
            return product

@app.put("/{id}", response_model=Product)
def update_product(id:int, data:Product):
    updated = get_product_by_id(id)

    updated["id"] = data["id"]
    updated["name"] = data["name"]
    updated["price"] = data["price"]

    return updated

@app.delete("/{id}", response_model=str)
def delete_product(id:int):
    deleted = get_product_by_id(id)

    PRODUCTS.pop(PRODUCTS.index(deleted))

    return f"Product with ID {id} deleted"