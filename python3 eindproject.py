import time
Books = {"The Lord of the Rings": "ISBN0a13p5k6T", "Harry Potter": "ISBN3w28c8z1O", "Oorlogswinter": "ISBN9x56q1o0Y", "Percy Jackson": "ISBN5s22t3t4W", "The Hunger games": "ISBN6w67m5g2P"}
bookStatus = {"The Lord of the Rings": ": present", "Harry Potter": ": present", "Oorlogswinter": ": present", "Percy Jackson":": present", "The Hunger games": ": present"}
menu = '''
Welcome to the library! Choose an option from the menu below.
Press 1 to:    Show the list of books
Press 2 to:    Add a books name and ISBN number to the list
Press 3 to:    Change a book name and ISBN number
Press 4 to:    Delete a book from the list
Press 5 to:    Borrow a book from the library
Press 6 to:    Bring back a borrowed book
Press 7 to:    Show the list of lent out books
'''
endProgram = 0
def continueProgram():
    input("Press enter to continue")
    
def printLibrary(doContinue):
    if doContinue == 0 or doContinue == 1:
        for key, value in Books.items():
            print(key, value)
    elif doContinue == 2 or doContinue == 3:
        for key, value in bookStatus.items():
            print(key, value)
    if doContinue == 0 or doContinue == 3:
        continueProgram()

def addBook():
    newBook = input("Type the book you want to add.")
    newISBN = input("Type the books ISBN number.")
    Books[newBook] = newISBN
    bookStatus[newBook] = ": present"
    
def changeBook():
    printLibrary(1)
    changingBook = input("Type the name of the book you want to change")
    editBook = input("Type the books new title")
    editISBN = input("Type the books new ISBN number")
    (Books[changingBook]) = editBook
    del Books[changingBook]
    del bookStatus[changingBook]
    Books[editBook] = editISBN
    bookStatus[editBook] = ": present"

def delBook():
    printLibrary(1)
    deletingBook = input("Which book do you want to delete?")
    del Books[deletingBook]
    del bookStatus[deletingBook]

def lendBook():
    printLibrary(2)
    lentoutBook = input("Which book do you want to lend out?")
    try:
        if bookStatus[lentoutBook] == ": present":
            bookStatus[lentoutBook] = ": lent out"
            print('''
            You have lent out the book!''')
            time.sleep(0.75)
        elif bookStatus[lentoutBook] == ": lent out":
            print('''
            That book has already been lent out!''')
            time.sleep(0.75)
    except:
        print('''
                That book doesn't exist!''')
        time.sleep(0.75)    

def bringbackBook():
    amountBorrowed = 0
    print("The books that have been lent out are:")
    for key, value in bookStatus.items():
        if value == ": lent out":
            print(key)
        else:
            amountBorrowed = amountBorrowed + 1
    if amountBorrowed == len(bookStatus):
        print('''
                There are no books that have been lent out''')
        time.sleep(0.75)
    else:
        bringbackBook = input("Type the name of the book you want to bring back") 
        bookStatus[bringbackBook] = ": present"
        print('''
                You have brought back the book!''')
        time.sleep(0.75)

def wrongNumber():
    print("Please enter a number from 1 to 7:")
    time.sleep(0.75)

def Menu():
    global Books
    menuChoice = input(menu)
    if menuChoice == "1":
        printLibrary(0)
    elif menuChoice == "2":
        addBook()
    elif menuChoice == "3":
        changeBook()
    elif menuChoice == "4":
        delBook()
    elif menuChoice == "5":
        lendBook()
    elif menuChoice == "6":
        bringbackBook()
    elif menuChoice == "7":
        printLibrary(3)
    else:
        wrongNumber()
while True:
    Menu()