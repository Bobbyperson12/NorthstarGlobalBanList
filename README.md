# NorthstartGlobalBanList

adds people from #ban-list in the northstar discord to your server's ban list

for right now this is all manually done so there is some degree of trust that you need to have for me

there really isn't an alternative that i can think of because each person would need a bot running to grab from the channel itself

i update the list on the site periodically but if i start slacking feel free to ping me (Bobbyperson#0026)

### Usage
1. put `banlist.py` in the same directory as `banlist.txt`

2. backup banlist.txt

3. run the script

alternatively, add this line to the beginning of your `r2ds.bat`

`py R2Northstar/autoupdate.py`

this will make the banlist update everytime you start your server, but you have to use `autoupdate.py` instead of `banlist.py`
#### Known bug
make sure your banlist has a new line at the end otherwise this script will act up

#### Contributing
if you feel that this script needs improving feel free to open an issue or pull request