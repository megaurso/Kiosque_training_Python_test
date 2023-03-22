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


def add_product(menu,**new_product):
    id = 1
    if not menu:
        new_product["_id"] = id

    for item_id in menu:
        if item_id["_id"] >= id:
            id = item_id["_id"] + 1


      
    new_product["_id"] = id

    menu.append(new_product)
    
    print(new_product)

    return new_product
    
