def hotel_cost(nights):
    return 140*nights
def plane_cost(city):
    if "Chittagong" == city:
        return 150
    elif "Dhaka" == city:
        return 200
    elif "Khulna" == city:
        return 250
    elif "Rajshahi" == city:
        return 300

def vehicle_cost(days):
    if days>=7:
        return 40*days-50
    elif days>=3:
        return 40*days-20
    else:
        return 40*days
def trip_cost(city,days,spending_money):
    return vehicle_cost(days)+hotel_cost(days)+plane_cost(city)+spending_money
print("The cost of vehicle: ",vehicle_cost(5))
print("The cost of plane: ",plane_cost("Dhaka"))
print("The cost of hotel: ",hotel_cost(7))
print("The total cost of the trip: ",trip_cost("Chittagong",6,500))

    

    
    