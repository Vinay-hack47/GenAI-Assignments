# Task 4: Combined Operations

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Webcam"]

categories = [
    "Electronics",
    "Accessories",
    "Accessories",
    "Electronics",
    "Accessories",
    "Electronics"
]

price_dict = {
    "Laptop": 55000,
    "Mouse": 450,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2000,
    "Webcam": 3000
}

catalog = []

for i in range(len(products)):
    catalog.append((products[i], price_dict[products[i]], categories[i]))

print("Catalog:", catalog)

category_to_products = {}

for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(product)

print("Category mapping:", category_to_products)

max_category = max(category_to_products, key=lambda c: len(category_to_products[c]))
print("Category with most products:", max_category)
print("Products:", category_to_products[max_category])
