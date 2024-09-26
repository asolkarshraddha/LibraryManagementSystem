class Library:
    def _init_(self):
        self.books = []

    def add_book(self):
        isbn = input("Enter ISBN: ")
        title = input("Enter title: ")
        author = input("Enter author: ")
        year = input("Enter publication year: ")

        book = {
            "isbn": isbn,
            "title": title,
            "author": author,
            "year": year,
            "available": True  # Mark the book as available initially
        }
        self.books.append(book)
        print(f"Book '{title}' added successfully!")

    def borrow_book(self):
        isbn = input("Enter the ISBN of the book you want to borrow: ")

        for book in self.books:
            if book["isbn"] == isbn:
                if book["available"]:
                    book["available"] = False
                    print(f"You've borrowed '{book['title']}'.")
                    return
                else:
                    print(f"Sorry, the book '{book['title']}' is currently unavailable.")
                    return
        print("Book not found!")

    def return_book(self):
        isbn = input("Enter the ISBN of the book you want to return: ")

        for book in self.books:
            if book["isbn"] == isbn:
                if not book["available"]:
                    book["available"] = True
                    print(f"Thank you for returning '{book['title']}'.")
                    return
                else:
                    print(f"Error: The book '{book['title']}' was not borrowed.")
                    return
        print("Book not found!")

    def view_available_books(self):
        available_books = [book for book in self.books if book["available"]]

        if not available_books:
            print("No books are currently available.")
        else:
            print("Available books:")
            for book in available_books:
                print(f"{book['title']} (ISBN: {book['isbn']}, Author: {book['author']}, Year: {book['year']})")