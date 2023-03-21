from menu import products

def get_product_by_id(id):
    for product in products:
        if product["_id"] == id:
            return product
    return {}


def get_products_by_type(type):
    result = []
    for product in products:
        if product["type"] == type:
            result.append(product)
    return result
