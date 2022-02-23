import requests
from pathlib import Path

banlist_path = Path.cwd() / "banlist.txt"

r = requests.get("http://140.82.61.159/banlist.txt")

with banlist_path.open("r+") as f:
    # read existing bans
    bans = set()
    for line in f:
        bans.add(line.strip())

    # read response bans
    for line in r.text.split("\n"):
        line = line.strip()
        # write if new
        if line not in bans:
            f.write(line + "\n")
            print("banned: " + line)
        else:
            print("already banned: " + line)