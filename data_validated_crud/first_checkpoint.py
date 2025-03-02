from fastapi import FastAPI

app = FastAPI()
PRODUCTS = []

@app.get("/")
def get_products():
    return PRODUCTS

@app.post("/")
def create_products():
    pass

@app.get("/{id}")
def get_product_by_id(id:int):
    pass

@app.put("/{id}")
def update_product(id:int):
    pass

@app.delete("/{id}")
def delete_product(id:int):
    pass