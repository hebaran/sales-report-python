def get_total_customer_spend(quantity: int, price: float) -> float:
    return quantity * price

def get_total_customers_spending(all_customers_data: list[dict[str, str | int | float]]) -> dict[str, float]:
    total_customers_spending_response = {}

    for customer_data in all_customers_data:
        customer_name = customer_data["customer"]
        quantity_purchased = customer_data["quantity"]
        product_price = customer_data["price"]
        total_customers_spending_response[customer_name] = total_customers_spending_response.get(customer_name, 0) + get_total_customer_spend(quantity_purchased, product_price)
    return total_customers_spending_response

def get_best_selling_product(all_customers_data: list[dict[str, str | int | float]]) -> dict[str, int]:
    all_selling_products = {}

    for customer_data in all_customers_data:
        product_purchased = customer_data["product"]
        quantity_purchased = customer_data["quantity"]
        all_selling_products[product_purchased] = all_selling_products.get(product_purchased, 0) + quantity_purchased
    best_selling_product_name = max(all_selling_products, key=all_selling_products.get)
    best_selling_product_quantity = all_selling_products[best_selling_product_name]
    best_selling_product_info_response = {best_selling_product_name: best_selling_product_quantity}
    return best_selling_product_info_response

def get_total_sold(all_customers_data: list[dict[str, str | int | float]]) -> float:
    total_sold_response = 0

    for customer_data in all_customers_data:
        quantity_purchased = customer_data["quantity"]
        product_price = customer_data["price"]
        total_sold_response += quantity_purchased * product_price
    return total_sold_response
