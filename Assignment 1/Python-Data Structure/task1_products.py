# Task 1: Product Collections (Lists & Tuples)

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Webcam"]

sample_product = ("Laptop", 55000, "Electronics")

print("2nd product:", products[1])
print("Last product:", products[-1])

products.append("Printer")
products.append("Router")
print("Updated products:", products)

temp = list(sample_product)
temp[1] = 52000
sample_product = tuple(temp)

print("Updated sample product:", sample_product)
