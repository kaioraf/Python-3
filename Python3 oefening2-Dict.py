Schoolvakken = {"Frans": "slecht", "Engels": "goed", "informatica": "leuk"}

for key, value in Schoolvakken.items():
    print(key, value)

if "Frans" in Schoolvakken:
    print("Frans bestaat :(")
else:
    print("Frans bestaat niet :)")