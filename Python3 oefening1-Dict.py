games = {"fortnite": "bad", "minecraft": "good"}

games["roblox"] = "meh"

print(games["minecraft"], games["roblox"])

del games["fortnite"]

if "fortnite" in games:
    print(games["fortnite"])
else:
    print("fortnite is weg!")
    
for key, value in games.items():
    print(key, value)
