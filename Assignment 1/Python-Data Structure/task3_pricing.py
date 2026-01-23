# Task 3: Product Pricing (Dictionaries)

price_dict = {
    "Laptop": 55000,
    "Mouse": 500,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2000,
    "Webcam": 3000
}

# Add product
price_dict["Printer"] = 8000

# Update price
price_dict["Mouse"] = 450

# Remove product safely
product = "Tablet"
if product in price_dict:
    del price_dict[product]
else:
    print(product, "not found")

print("Price dictionary:", price_dict)

average_price = sum(price_dict.values()) / len(price_dict)
print("Average price:", average_price)

max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)

print("Most expensive:", max_product, price_dict[max_product])
print("Cheapest:", min_product, price_dict[min_product])
