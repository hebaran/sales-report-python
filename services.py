def get_total_customer_spend(customer_data: tuple[int, float]) -> float:
    amount, price = customer_data
    return amount * price

def get_total_customers_spending(all_customers_data:list[tuple[str, str, int, float]]) -> dict[str, float]:
    total_customers_spending_response = {}

    for customer_name, _, quantity_purchased, product_price in all_customers_data:
        customer_spend_data = (quantity_purchased, product_price)
        total_customers_spending_response[customer_name] = total_customers_spending_response.get(customer_name, 0) + get_total_customer_spend(customer_spend_data)
    return total_customers_spending_response

def get_best_selling_product(all_customers_data:list[tuple[str, str, int, float]]) -> dict[str, int]:
    all_selling_products = {}

    for _, product_purchased, quantity_purchased, _ in all_customers_data:
        all_selling_products[product_purchased] = all_selling_products.get(product_purchased, 0) + quantity_purchased
    best_selling_product_name = max(all_selling_products, key=all_selling_products.get)
    best_selling_product_quantity = all_selling_products[best_selling_product_name]
    best_selling_product_info_response = {best_selling_product_name: best_selling_product_quantity}
    return best_selling_product_info_response

def get_total_sold(all_customers_data:list[tuple[str, str, int, float]]) -> float:
    total_sold_response = 0
    for _, _, product_quantity, product_price in all_customers_data:
        total_sold_response += product_quantity * product_price
    return total_sold_response
