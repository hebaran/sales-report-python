def show_customers_spending(customers_spending_data: dict[str, float]) -> None:
    for customer_name, customer_spend in customers_spending_data.items():
        print(f"{customer_name} -> R$ {customer_spend:,.2f}")

def show_best_selling_product(best_selling_product_info: dict[str, int]) -> None:
    (product_name, product_quantity), = best_selling_product_info.items()
    print(f"Produto mais vendido: {product_name} ({product_quantity} unidades)")

def show_total_sold(total_sold_value: float) -> None:
    print(f"Total vendido: R$ {total_sold_value:,.2f}")
