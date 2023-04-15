import requests as r


def getproducts(products):
    x = r.get(f'https://fakestoreapi.com/products/{products}')
    d = x.json()
    print(d)
    product = {
        'product_id' : data["id"],
        'product_name' : data["title"],
        'price' : data["price"],
        'description' : data["description"],
        'category': data["category"],
        'product_image' : data["image"]
        }
    return product
    


