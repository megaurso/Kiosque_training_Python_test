from menu import products
from collections import Counter


def get_product_by_id(id: int):
    if not isinstance(id, int):
        raise TypeError("product id must be an int")

    for product in products:
        if product["_id"] == id:
            return product
    return {}


def get_products_by_type(type: str):
    if not isinstance(type, str):
        raise TypeError("product type must be a str")

    result = []
    for product in products:
        if product["type"] == type:
            result.append(product)
    return result


def add_product(menu, **new_product):
    id = 1
    if not menu:
        new_product["_id"] = id

    for item_id in menu:
        if item_id["_id"] >= id:
            id = item_id["_id"] + 1

    new_product["_id"] = id

    menu.append(new_product)

    return new_product


def menu_report():
    product_count = 0
    price = 0

    for index, value in enumerate(products):
        product_count = index + 1

    for product in products:
        price += product["price"]

    average_price = price / product_count

    counter = Counter(product["type"] for product in products)

    most_common_type = counter.most_common(1)[0][0]

    return f"Products Count: {product_count} - Average Price: ${round(average_price,2)} - Most Common Type: {most_common_type}"


def add_product_extra(menu, *required_keys, **new_product):
    id = 1
    for key in required_keys:
        if key not in new_product:
            raise KeyError(f"field {key} is required")

    extra_key = set(new_product.keys()).symmetric_difference(set(required_keys))

    for key in extra_key:
        new_product.pop(key)

    if not menu:
        new_product["_id"] = id

    for item_id in menu:
        if item_id["_id"] >= id:
            id = item_id["_id"] + 1

    new_product["_id"] = id

    menu.append(new_product)

    return new_product
