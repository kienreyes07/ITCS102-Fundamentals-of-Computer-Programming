#shipping chalenge

sender = input("Sender's Name: ")
type = input("Type of Item: ")
is_fragile = bool(input("Is this product fragile? (yes/no) ") == "yes")
weight = float(input("Enter Weight of item (kg): "))
distance = float(input("Enter Distance (km): "))
is_express = bool(input("Is it express delivery? (yes/no) ") == "yes")
is_international = bool(input("Is it international delivery? (yes/no) ") == "yes")
tota = 0

base_cost = (weight * 2.5) + (distance * 0.15)


if weight <= 2.0 and distance <= 100 and not is_express and not is_international:
    total = 0

elif is_international and is_express:
    total = (base_cost * 1.40) + 50

elif is_express or (is_international and weight > 20):
    total = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000:
    total = base_cost + 30

else:
    total = base_cost


print()
print("================================ SHIPPING SUMMARY ================================")
print("\tTotal Cost is: PHP", total)