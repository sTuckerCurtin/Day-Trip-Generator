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

#display_list(destinations)
#display_list(restaurants)
#display_list(entertainments)
#display_list(transportations)



def trip_generator(list1, list2, list3):
    for trips in list1:
        random_trip1 = random.choice(list1)
    for trips in list2:
        random_trip2 = random.choice(list2)
    for trips in list3:
            random_trip3 = random.choice(list3)
    print(random_trip1, random_trip2, random_trip3)
    return trip_generator

trip_generator(destinations, transportations, entertainments)