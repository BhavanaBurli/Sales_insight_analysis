sales_data = [
    {"product": "Soap", "quantity": 10, "price": 30},
    {"product": "Shampoo", "quantity": 5, "price": 100},
    {"product": "Toothpaste", "quantity": 8, "price": 40},
    {"product": "Soap", "quantity": 15, "price": 30},
    {"product": "Shampoo", "quantity": 3, "price": 100},
    {"product": "Toothpaste", "quantity": 4, "price": 40}
]
total_revenue = 0

for sale in sales_data:
    total_revenue += sale["quantity"] * sale["price"]

print("Total Revenue:", total_revenue)
product_summary = {}

for sale in sales_data:
    product = sale["product"]
    quantity = sale["quantity"]
    revenue = sale["quantity"] * sale["price"]

    if product not in product_summary:
        product_summary[product] = {"total_quantity": 0, "total_revenue": 0}

    product_summary[product]["total_quantity"] += quantity
    product_summary[product]["total_revenue"] += revenue

# Display the summary
print("\nProduct-wise Summary:")
for product, summary in product_summary.items():
    print(f"{product}: Quantity Sold = {summary['total_quantity']}, Revenue = ₹{summary['total_revenue']}")
best_product = ""
max_quantity = 0

for product, summary in product_summary.items():
    if summary["total_quantity"] > max_quantity:
        max_quantity = summary["total_quantity"]
        best_product = product

print(f"\nBest-Selling Product: {best_product} (Sold {max_quantity} units)")
