destinations = ["Mexico", "New York", "Buffalo", "Cleveland"] 
restaurants = ["Steak House", "Gastropub", "Diner", "Deli"] 
transportations = ["Plane", "Train", "Automobile"] 
entertainments = ["See a show", "Go to a Museam", "Explore the City", "Relax"]

import random

# def display_list(list):
#     for item in list:
#         random_item = random.choice(list)
#         print(random_item)
#         return display_list

#display_list(destinations)
#display_list(restaurants)
#display_list(entertainments)
#display_list(transportations)
#destinaton = random.choice(destinations)


# def trip_generator(list1, list2, list3, list4):
#     for trips in list1:
#         random_trip1 = random.choice(list1)
#     for trips in list2:
#         random_trip2 = random.choice(list2)
#     for trips in list3:
#             random_trip3 = random.choice(list3)
#     for trips in list4:
#             random_trip4 = random.choice(list4)
#     print(random_trip1, random_trip2, random_trip3, random_trip4)
#     print("Here is  your completed Trip")
#     return 

# trip_generator(destinations, transportations, entertainments, restaurants)


def trip_generator(destinations, restaurants, transportations, entertainments):
    destination = random.choice(destinations)
    restaurant = random.choice(restaurants)
    transportation = random.choice(transportations)
    entertainment = random.choice(entertainments)
    print(destination, restaurant, transportation, entertainment)
    print("Here is your complted trip")

trip_generator(destinations, restaurants, transportations, entertainments)



# def trip_generator(destinations, restaurants, transportations, entertainments):
#     full_trip = random.choice(destinations), random.choice(restaurants), random.choice(transportations), random.choice(entertainments)
#     print(full_trip)