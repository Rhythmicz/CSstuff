from collections import deque  # implements .pop() and .popleft() for lists


class Patron(object):
    def __init__(self, name): #Constructs the default attributes a patron has.
        self.name = name
        self.booksout = 0 # The numbers of books a patron has
        self.book = None # books currently borrowed
        self.pastbooks = [] # Past books borrowed

    def addBook(self):
        self.booksout += 1 # Adds +1 to the book count 

    def subBook(self):
        self.booksout -= 1 # subtracts -1 from the book count

    def getBooksout(self):
        return self.booksout # Gets the number of books

    def getPastbooks(self):
        return self.pastbooks # Getes the list of books a patron has borrowed

    def __str__(self): # The string that is outputted whenever the class patron is called on.
        string = (f"{self.name} has {str(self.booksout)} books.")  
        return string


class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrower = None # Whom the book is currently borrowed by.
        self.waitlist = deque([]) # Waitlist which contains a list of the __str__ from the Patron class
        self.waitlistNames = deque([]) # Waitlist which contains the list of patrons that are of class Patron
    def getWaitlist(self): 
        return self.waitlist

    def getWaitlistNames(self):
        return self.waitlistNames

    def getBorrower(self):
        return self.borrower

    def setBorrower(self, patron): #setter which allows for changes of the books borrower
        self.borrower = patron

    def __str__(self): # String for whenever the book class is called
        string2 = (
            f"{self.title}, {self.author} in care of: {str(self.borrower)}\nWaiting: \n" #string for when book has a borrower
        )
        string4 = (
            f"{self.title}, {self.author} and has not been borrowed.\nWaiting:  \n" #string for when book has no borrower
        )
        if self.borrower != None: #if book has a borrower
            if len(self.waitlist) > 0: #waitlist length is longer than 0
                for index in range(0, len(self.waitlist)): 
                    string2 += f"{index+1}. {self.waitlist[index]} \n" # Adds to string 2 the numbering of the waitlist and outputs the string of the patron in the waitlist.
                return string2
            else:  # borrower != None and len == 0
                return string2
        elif self.borrower == None:  
            if len(self.waitlist) > 0:
                for index in range(0, len(self.waitlist)):
                    string4 += f"{index+1}. {self.waitlist[index]}\n" # Adds to string 4 the numbering of the waitlist and outputs the string of the patron in the waitlist.
                return string4
            else:  # borrower == None and len == 0
                return string4


class Library(object):
    def __init__(self, books):
        self.books = books #List of books in the library. These are of class Book
        self.patrons = [] # List of patrons in the library. These are of class Patron

    def addBook(self, book): #adds a book to the library 
        self.books.append(book)

    def addPatron(self, patron): #adds a patron to library 
        self.patrons.append(patron)

    def removeBook(self, book): # Removes a book from the library
        self.books.remove(book)
        print(f"{str(book.title)}, {str(book.author)} removed from the library!\n")

    def removePatron(self, patron): # Removes a patron from the library
        self.patrons.remove(patron)
        print("Patron removed!\n")

    def findBook(self, book): #Finds books in the library
        if book in self.books: # If book present in library
            if book.getBorrower() == None: # and book has no borrower
                print("Available for checkout!") # output
            else:
                print(f"{str(book)}") 
        else: #Book not found in library
            print(f"{str(book.title)}, {str(book.author)} is not in the library")

    def findPatron(self, patron):
        if patron in self.patrons:
            print(f"{str(patron.name)} found in the database! \n")
        else:
            print(f"The user '{str(patron.name)}' NOT found in the database! \n")

    def borrowBook(self, book, patron): # Borrow book from library
        if book.getBorrower() == None: # If book has no borrower
            if patron.getBooksout() < 3: # and patrons book count is less than 3
                book.setBorrower(patron) # set the books borrower as the patron
                patron.addBook() # add +1 to the patrons book count
            else:
                print("Can't borrow more books-- MAX REACHED") # Patron has >= 3 books checked out already
        else:
            book.waitlist.append(str(patron)) #Add the __str__ of the patron  to the waitlist
            book.waitlistNames.append(patron) #Add the Patron class to the waitlist

    def returnBook(self, book):
        if len(book.getWaitlistNames()) > 0:
            book.borrower.subBook()  # books current borrower subtract 1 from the book count
            print(f"Returned: {str(book)}\n")
            book.borrower = None # set the books owner to None

            """
            The code below is what I'd use to implement a que system that automatically assigns the first 
            person in the waitilist as the borrower which then moves the queue forward by popping left the
            first person to enter the list. In the interest of keeping the associate output the same as the labs,
            I have not included it.
            """

            # book.setBorrower(book.waitlistNames[0]) #set books new borrower as the first person in the waitlist
            # book.waitlistNames[0].addBook() #add 1 to the book count of the first person in the wait list
            # book.waitlist.popleft() #popleft the list
            # book.waitlistNames.popleft() #popleft the list
        else:
            book.borrower.subBook()
            print(f"Returned: {str(book)}")
            book.borrower = None

    def __str__(self): # string when the library class is called
        string3 = "Books: \n"
        for index in self.books: # iterates through the books in the library
            string3 += f"{str(index)} \n" #adds to string3 the __str__ of each book class
        string3 += f"Patrons: \n"  # adds to string 3
        for index in self.patrons: # iterates through the patrons in the library
            string3 += f"{index}\n" #adds to string3 the __str__ of each patron  class
        return string3

"""
Trae Taylor

06/12/2020

This program adds a Library class that manages the Book and Patron classes developed in Exercise 1. The library
includes the methods for adding, removing, and finding books and patrons. Additionally, methods for borrowing and
returning a book are included.

Input: Books or Patrons of class Book and class Patron

Output: Books in the library, patrons in the library, waitlist of books, # of books a patron has checked out. Testing of 
addBook, addPatron, removeBook, removePatron, findbook, and findPatron are also included.

"""

def main():
    
    book1 = Book("Of Mice and Men", "Steinbeck")
    book2 = Book("The Great Gatsby", "Fitzgerald")
    book3 = Book("1984", "Orwell")
    book4 = Book("One Flew Over the Cuckoo's Nest", "Kesey")

    libraryBooks = []
    libraryBooks.append(book1)
    libraryBooks.append(book2)
    libraryBooks.append(book3)
    libraryBooks.append(book4)

    patron1 = Patron("Ivan")
    patron2 = Patron("Jimmy")
    patron3 = Patron("Bob")

    myLibrary = Library(libraryBooks)
    myLibrary.addPatron(patron1)
    myLibrary.addPatron(patron2)
    myLibrary.addPatron(patron3)

    myLibrary.borrowBook(book1, patron2)
    myLibrary.borrowBook(book1, patron3)

    print(str(myLibrary))
    myLibrary.returnBook(book1)
    print(str(myLibrary))

    print(
        "====================================================================================================="
    )
    print("\nTesting addBook\n")
    print(
        "=====================================================================================================\n"
    )

    book5 = Book("Win Friends & Influence People", "Dale Carnegie")
    myLibrary.addBook(book5)
    print(str(myLibrary))

    print(
        "====================================================================================================="
    )
    print("\nTesting addPatron\n")
    print(
        "=====================================================================================================\n"
    )

    patron4 = Patron("Trae")
    myLibrary.addPatron(patron4)
    print(str(myLibrary))

    print(
        "====================================================================================================="
    )
    print("\nTesting removeBook\n")
    print(
        "=====================================================================================================\n"
    )

    myLibrary.removeBook(book5)
    print(str(myLibrary))

    print(
        "====================================================================================================="
    )
    print("\nTesting removePatron\n")
    print(
        "=====================================================================================================\n"
    )

    myLibrary.removePatron(patron4)
    print(str(myLibrary))

    print(
        "====================================================================================================="
    )
    print("\nTesting findBook\n")
    print(
        "=====================================================================================================\n"
    )

    myLibrary.findBook(book4)
    myLibrary.findBook(book5)

    print(
        "\n====================================================================================================="
    )
    print("\nTesting findPatron\n")
    print(
        "=====================================================================================================\n"
    )

    myLibrary.findPatron(patron4)
    myLibrary.findPatron(patron3)


main()
