class Book:


    def __init__(self, title, author, genre, isbn, pages):
        """
        Initializes a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            genre (str): The genre of the book (e.g., "Fiction", "Non-Fiction", "Mystery").
            isbn (str): The ISBN (International Standard Book Number).
            pages (int): The number of pages in the book.
        """
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.pages = pages
        self.is_borrowed = False

    def borrow(self):
        """Marks the book as borrowed."""
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"{self.title} by {self.author} has been borrowed.")
        else:
            print(f"{self.title} is already borrowed.")

    def return_book(self):
        """Marks the book as returned."""
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"{self.title} by {self.author} has been returned.")
        else:
            print(f"{self.title} is not currently borrowed.")

the_hobbit = Book("The Hobbit", "J.R.R. Tolkien", "Fantasy", "9780261103757", 295)
the_hobbit.borrow()
the_hobbit.borrow()  # Should print that the book is already borrowed
the_hobbit.return_book()