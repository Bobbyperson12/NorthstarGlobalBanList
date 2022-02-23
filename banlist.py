import requests
import os

url = "http://140.82.61.159/banlist.txt"
# ban list

r = requests.get(url)
#retrieving data from the URL using get method

with open("temp.txt", 'wb') as f:
#giving a name and saving it in any required format
#opening the file in write mode

    f.write(r.content) 
    f.close()
#writes the URL contents from the server

# open the data file
file = open("temp.txt")
# read the file as a list
data = file.readlines()
# close the file
file.close()

newdata = []
# clean file from \n
for ban in data:
    ban = ban.strip('\n')
    newdata.append(ban)

#print(data) #debug
#print(newdata) #debug

with open('banlist.txt') as f:
    file_lines = [line.rstrip() for line in f.readlines()] # spooky code that does spooky things to make this work

with open("banlist.txt", "a+") as file: 
    for item in newdata: 
        if item not in file_lines:
            file.write(item + "\n")
            print("banned: " + item)
        else:
            print("already banned: " + item)

os.remove("temp.txt") # cleanup