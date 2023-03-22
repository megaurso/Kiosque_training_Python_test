from menu import products
def calculate_tab(dic):
    total = 0
    for ids in dic:
        for product in products:
            if ids["_id"] == product["_id"]:
                total += ids["amount"] * product["price"]

    account = {
        "subtotal" : f"${round(total,2)}"
    }


    return account
