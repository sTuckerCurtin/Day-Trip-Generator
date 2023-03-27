destinations = ["Mexico", "New York", "Buffalo", "Cleveland"] 
restaurants = ["Steak House", "Gastropub", "Diner", "Deli"] 
transportations = ["Plane", "Train", "Automobile"] 
entertainments = ["See a show", "Go to a Museam", "Explore the City", "Relax"]

import random

def display_list(list):
     for item in list:
         random_item = random.choice(list)
         print(random_item)
         return display_list

# display_list(destinations)
# display_list(restaurants)
# display_list(entertainments)
# display_list(transportations)


# def trip_generator(destinations, restaurants, transportations, entertainments):
#     destination = random.choice(destinations)
#     restaurant = random.choice(restaurants)
#     transportation = random.choice(transportations)
#     entertainment = random.choice(entertainments)
   
#     print("Here is your potential Day Trip ")
#     print(f"Destination : {destination}")
#     print(f"Restaurant: {restaurant}")
#     print(f"Transportation: {transportation}")
#     print(f"Entertainment: {entertainment}")
#     trip_confirmation = input("Do you want to confirm this trip? y/n ")
#     if trip_confirmation == "y":
#          print("Trip Confrimed")
#     else:
#         trip_generator(destinations, restaurants, transportations, entertainments)
    
    



# trip_generator(destinations, restaurants, transportations, entertainments)

def random_choice(list):
    return random.choice(list)


def print_trip(destination, restaurant, transportation, entertainment):
    print("Here is your potential Day Trip ")
    print(f"Destination : {destination}")
    print(f"Restaurant: {restaurant}")
    print(f"Transportation: {transportation}")
    print(f"Entertainment: {entertainment}")


def confrim_trip():
    trip_confirmation = input("Do you want to confirm this trip? y/n ")
    if trip_confirmation == "y":
          print("Trip Confrimed")
    else:
         trip_generator(destinations, restaurants, transportations, entertainments)
     



def trip_generator(destinations, restaurants, transportations, entertainments):
    destination = random_choice(destinations)
    restaurant = random_choice(restaurants)
    transportation = random_choice(transportations)
    entertainment = random_choice(entertainments)
    print_trip(destination, restaurant, transportation, entertainment)
    confrim_trip()




trip_generator(destinations, restaurants, transportations, entertainments)

