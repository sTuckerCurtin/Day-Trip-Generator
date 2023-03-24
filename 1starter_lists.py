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


display_list(destinations)