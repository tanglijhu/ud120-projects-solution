#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import re
import os

width = os.get_terminal_size().columns

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
print("\n")
print_text = "Number of people: " + str(len(enron_data))
print(print_text.center(width))

print_text = "Features: " + str(len(enron_data[list(enron_data.keys())[0]]))
print(print_text.center(width))

enron_dataset_poi_counter = 0
names = list(enron_data.keys())

for i in range(len(enron_data)):
    if enron_data[names[i]]["poi"] == 1:
        enron_dataset_poi_counter += 1
print_text = "Number of POI in enron dataset: " + str(enron_dataset_poi_counter)
print(print_text.center(width))




with open("../final_project/poi_names.txt") as f:
    contents = f.readlines()
f.close()

poi_list_poi_counter = 0
for content in contents:
    if re.match( r'\((y|n)\)', content):
        poi_list_poi_counter += 1

print_text = "Number of POI in poi-list: " + str(poi_list_poi_counter)
print(print_text.center(width))


print("\n")