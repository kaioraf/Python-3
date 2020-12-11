numbers = {}
count = 1
amount = int(input("How many numbers do you want squared?"))

def calculation():
    global count
    global amount
    amount = amount + 1
    while count != amount:
        numbers[count] = count*count
        count = count + 1
    for key, value in numbers.items():
        print(key, value)
    
calculation()