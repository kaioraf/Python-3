def printer(number, string):
    for i in range(number):
        print(string)
        
string = input("Which character")
number = int(input("How many times"))
printer(number, string)
