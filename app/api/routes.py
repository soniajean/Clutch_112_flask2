from flask import Blueprint, request
from ..models import Product

api = Blueprint('api', __name__, url_prefix='/api')



@api.route('/products')
def getProds():
    prods = Product.query.all()
    prodlist = [p.to_dict() for p in prods]
    return {
        'status': 'ok',
        'data' : prodlist,
        'item_count' : len(prodlist)
    }

@api.route('/product/<int:prod_id>')
def getIndProd(prod_id):
    p = Product.query.get(prod_id)
    if p:
        prod = p.to_dict()
        return {
            'status': 'ok',
            'data': prod,
        }
    return {
        'status': 'Error',
        'message': 'No product with that ID exists',
    }

@api.post('/createproduct')
def createProductAPI():
    data = request.json # This coming from the POST request body

    title = data['title']
    price = data['price']
    description = data['description']
    category = data['category']
    img_url = data['img_url']
   

    new = Product(title, price, description, category, img_url)
    new.saveProduct()
    return {
        'status' : 'ok',
        'message' : 'new product has been created!'
    }
