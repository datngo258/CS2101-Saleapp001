from models import Product, Category

def get_category():
    return Category.query.all()
def get_product():
    return Product.query.all()
