from services import get_total_customers_spending, get_best_selling_product, get_total_sold
from views import show_customers_spending, show_best_selling_product, show_total_sold
import json

with open("customers.json", "r", encoding="UTF-8") as data:
    customers_data = json.load(data)

total_customers_spending = get_total_customers_spending(customers_data)
show_customers_spending(total_customers_spending)
best_selling_product = get_best_selling_product(customers_data)
show_best_selling_product(best_selling_product)
total_sold = get_total_sold(customers_data)
show_total_sold(total_sold)
