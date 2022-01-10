"""
Create a library class
display Book
lend book
add book
return book
harrylibrary = library(listbook)
dictionary (books-nameof person) """


class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBook(self):
        print(f"We Have Following Books In Our Library: {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            self.booksList.remove(book)
            print("Lender_Book database has been updated. You can take the book now")


        else:
            print(f"Book is already being used by {self.lendDict[book]}")


    def addBoook(self, book):
        self.booksList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)
        self.booksList.append(book)



if __name__ == '__main__':
    Sidharaj = Library(['Python', 'c Lang', 'c++', 'HTML', 'Java Pro'], "Code_Hub")

    while(True):
        print(f"Welcome to the {Sidharaj.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            Sidharaj.displayBook()

        elif user_choice == 2:
            book = input("Enter the name of book you want to lend:")
            user = input("Enter your name")
            Sidharaj.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            Sidharaj.addBoook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            Sidharaj.returnBook(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":

            #else: user_choice2 =="c":
                continue


