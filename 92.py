'''
create a python online library which is able to issue books, add books, return books, show available books.
'''
import datetime
LibStorage = []
class book:
    def __init__(self, name, author):
        self.Name = name
        self.author = author
        self.isIssued = False
        self.Issuedto = "NOT_YET_ISSUED"
        self.issuedOn = "NOT_YET_ISSUED"
    def __str__(self) -> str:
        return self.Name

class lib:
    def addBook(self, Name, Author):
        bookObj = book(Name, Author)
        LibStorage.append(bookObj)
        return bookObj
    def issueBook(self, name, book):
        if book.isIssued:
            print("The book is already issued to ", book.Issuedto)
        else:
            book.isIssued = True
            book.Issuedto = name
            book.issuedOn = datetime.datetime.now()
            LibStorage.remove(book)
            print("The book sucessfully issued!")
    def returnBook(self, book):
        if not book.isIssued:
            print("ERROR! The book is not yet issued unable to return.")
        else: 
            LibStorage.append(book)
            book.issuedOn = "NOT_YET_ISSUED"
            book.isIssued = False
            book.Issuedto = "NOT_YET_ISSUED"
            print("The book sucessfully returned!")

    def showAvailableBooks(self):
        for item in LibStorage:
            print(item, end=", ")
        print()

library = lib()
MyCoding = library.addBook("My coding", "Devansh")
WingsOfFire = library.addBook("Wings of fire", "APJ Abdul Kalam")
LongWalkToFreedom = library.addBook("Long walk to freedom", "Nelson Mandela")
library.showAvailableBooks()
library.issueBook("Devansh", MyCoding)
library.showAvailableBooks()
# print(MyCoding.issuedOn)
library.returnBook(MyCoding)
library.returnBook(LongWalkToFreedom)
library.showAvailableBooks()
