# Lab 01 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):
    total_distance = one_way_km * 2
    fuel_needed = total_distance / km_per_liter
    total_cost = fuel_needed * price_per_liter

    return total_cost <= budget

# Test your code here
print("Testing Road Trip Budgeter...")
print (is_budget_sufficient(100, 10, 2.00, 40))
print (is_budget_sufficient(100, 10, 2.00, 39))