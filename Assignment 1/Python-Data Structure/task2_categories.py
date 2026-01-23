# Task 2: Categories (Sets)

categories = [
    "Electronics",
    "Accessories",
    "Accessories",
    "Electronics",
    "Accessories",
    "Electronics"
]

categories_set = set(categories)
print("Initial categories:", categories_set)

categories_set.add("Furniture")
categories_set.add("Electronics")  # duplicate ignored

print("After adding:", categories_set)

print("Is 'Furniture' present?", "Furniture" in categories_set)

print("Total unique categories:", len(categories_set))
