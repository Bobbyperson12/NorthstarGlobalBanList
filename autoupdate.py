import requests
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

url = "http://140.82.61.159/banlist.txt" # ban list

r = requests.get(url) # retrieving data from the URL using get method

with open(os.path.join(__location__, "temp.txt"), 'wb') as f: # giving a name and saving it
    f.write(r.content) # writes the URL contents from the server

file = open(os.path.join(__location__, "temp.txt")) # open the data file
data = [line.strip() for line in file.readlines()] # read the file as a list and clean
file.close() # close the file

with open(os.path.join(__location__, "banlist.txt")) as f:
    file_lines = [line.rstrip() for line in f.readlines()] # spooky code that does spooky things to make this work

with open(os.path.join(__location__, "banlist.txt"), "a+") as file: 
    for item in data: 
        if item not in file_lines:
            file.write(item + "\n")
            print("banned: " + item)
        else:
            print("already banned: " + item)

os.remove(os.path.join(__location__, "temp.txt")) # cleanup