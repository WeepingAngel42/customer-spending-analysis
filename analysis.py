customers = [
    {"name": "Alice", "age": 30, "city": "Portland", "money": 100},
    {"name": "Bob", "age": 22, "city": "Seattle", "money": 40},
    {"name": "Carol", "age": 35, "city": "Portland", "money": 60},
    {"name": "Dave", "age": 28, "city": "Seattle", "money": 20}
]

item_cost = 50

def customers_who_can_afford(customers, item_cost):
    result = []
    for person in customers:
        if person["money"] >= item_cost:
            result.append(person["name"])
    return result


def high_value_customers(customers):
    result = []
    for person in customers:
        if person["money"] > 80:
            result.append(person["name"])
    return result


def customers_needing_discount(customers, item_cost):
    result = []
    for person in customers:
        if person["money"] < item_cost:
            result.append(person["name"])
    return result


print("Customers who can afford the item:")
print(customers_who_can_afford(customers, item_cost))

print("\nHigh value customers:")
print(high_value_customers(customers))

print("\nCustomers needing discount:")
print(customers_needing_discount(customers, item_cost))
