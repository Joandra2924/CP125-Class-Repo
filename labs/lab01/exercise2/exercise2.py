# Lab 01 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price):
    numOfTents = math.ceil(participants / tent_capacity)
    totalCost = numOfTents * tent_price
    return totalCost

# Test your code here
print("Testing Camping Logistics...")
print(calculate_event_cost(12, 4, 100))
print(calculate_event_cost(13, 4, 100))