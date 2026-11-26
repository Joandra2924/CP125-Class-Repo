# Lab 01 Exercise 1: Road Trip Budgeter
def is_budget_sufficient(one_way_km, budget):
    round_trip = one_way_km * 2
    litres = round_trip / 10
    price = litres * 2
    return price <= budget

print(is_budget_sufficient(100, 40))
print(is_budget_sufficient(100, 39))