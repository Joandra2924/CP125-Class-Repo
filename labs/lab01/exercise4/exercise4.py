# Lab 01 Exercise 4: Dynamic Parking Rate
def get_hourly_rate(vehicle_type, hour):

    if vehicle_type == "Electric":
        price = 2

    elif vehicle_type == "Hybrid":
        if (hour > 21) or (hour < 7):
            price = 2
        else :
            price = 5

    else :
        price = 5

    return price