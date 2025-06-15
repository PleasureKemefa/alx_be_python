# programming_paradigm/library_management.py

class Book:
    """Represents a book with title, author, and availability status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is not checked out."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of Book objects."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)
        
    def check_out_book(self, title):
        """Mark a book as checked out by title, if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        """Return a book to the library by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"Book '{title}' was not checked out or doesn't exist.")

    def list_available_books(self):
        """Print all available books in the library."""
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No books are currently available.")
        else:
            for book in available:
                print(book)    