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

def show_customers_spending(customers_spending_data: dict[str, float]) -> None:
    for customer_name, customer_spend in customers_spending_data.items():
        print(f"{customer_name} -> R$ {customer_spend:,.2f}")

def show_best_selling_product(best_selling_product_info: dict[str, int]) -> None:
    (product_name, product_quantity), = best_selling_product_info.items()
    print(f"Produto mais vendido: {product_name} ({product_quantity} unidades)")

def show_total_sold(total_sold_value: float) -> None:
    print(f"Total vendido: R$ {total_sold_value:,.2f}")


customers_data = [
  ("Pedro", "Hamburguer", 2, 25.50),
  ("Maria", "Refrigerante", 1, 8.00),
  ("Pedro", "Batata Frita", 1, 12.00),
  ("João", "Hamburguer", 1, 25.50),
  ("Maria", "Sorvete", 3, 10.00)
]

total_customers_spending = get_total_customers_spending(customers_data)
show_customers_spending(total_customers_spending)
best_selling_product = get_best_selling_product(customers_data)
show_best_selling_product(best_selling_product)
total_sold = get_total_sold(customers_data)
show_total_sold(total_sold)
