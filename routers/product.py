from fastapi import APIRouter, HTTPException

from schema.product import Product, ProductCreate, products

product_router = APIRouter()

# create product
# list all products

@product_router.post('/', status_code=201)
def create_product(payload: ProductCreate):
    # get the product id
    product_id = len(products) + 1
    new_product = Product(
        id=product_id,
        name=payload.name,
        price=payload.price,
        quantity_available=payload.quantity_available
    )
    products[product_id] = new_product
    return {'message': 'Product created successfully', 'data': new_product}


@product_router.get('/', status_code=200)
def list_products():
    return {'message': 'success', 'data': products}


@product_router.put('/{product_id}', status_code=200)
def update_product(product_id: int, payload: ProductCreate):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product = products[product_id]
    product.name = payload.name
    product.price = payload.price
    product.quantity_available = payload.quantity_available
    
    return {'message': 'Product updated successfully', 'data': product}



