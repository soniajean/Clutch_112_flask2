import requests as r


def getproducts(products):
    x = r.get(f'https://fakestoreapi.com/products/{products}')
    d = x.json()
    # print(d)
    product = {}
    id = d['products'][0]['id']
    title = d['products'][0]['title']
    price = d['products'][0]['price']
    description = d['products'][0]['description']
    category = d['products'][0]['caategory']
    img_url = d['products'][0]['img_url']

    product['id'] = id
    product['title'] = title
    product['price'] = price
    product['description'] = description
    product['category'] = category
    product['img_url'] = img_url

    return product
    


