# Library Management System

class Book:
    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages

    # Getter for title
    def get_title(self):
        return self._title

    # Setter for title
    def set_title(self, title):
        self._title = title

    # Getter for author
    def get_author(self):
        return self._author

    # Setter for author
    def set_author(self, author):
        self._author = author

    # Getter for pages
    def get_pages(self):
        return self._pages

    # Setter for pages
    def set_pages(self, pages):
        self._pages = pages

    # Class method to calculate reading time based on a reading speed of 250 words per minute
    @classmethod
    def calculate_reading_time(cls, pages, words_per_page=300, reading_speed=250):
        total_words = pages * words_per_page
        return total_words / reading_speed

    # String representation of the Book
    def __str__(self):
        return f"Title: {self._title}, Author: {self._author}, Pages: {self._pages}"


class Ebook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self._format = format

    # Getter for format
    def get_format(self):
        return self._format

    # Setter for format
    def set_format(self, format):
        self._format = format

    # Overriding the __str__ method to include format
    def __str__(self):
        return f"Title: {self._title}, Author: {self._author}, Pages: {self._pages}, Format: {self._format}"


# Demonstration of usage
if __name__ == "__main__":
    try:
        # Creating an instance of Book
        my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)

        # Using getters
        print(my_book.get_title())  # Output: The Great Gatsby
        print(my_book.get_author())  # Output: F. Scott Fitzgerald
        print(my_book.get_pages())  # Output: 180

        # Using setters
        my_book.set_title("1984")
        my_book.set_author("George Orwell")
        my_book.set_pages(328)

        # Using getters again to see the changes
        print(my_book.get_title())  # Output: 1984
        print(my_book.get_author())  # Output: George Orwell
        print(my_book.get_pages())  # Output: 328

        # Calculating reading time
        reading_time = Book.calculate_reading_time(my_book.get_pages())
        print(f"Estimated reading time: {reading_time} minutes")  # Output: Estimated reading time: 393.6 minutes

        # Creating an instance of Ebook
        my_ebook = Ebook("1984", "George Orwell", 328, "PDF")
        print(my_ebook)  # Output: Title: 1984, Author: George Orwell, Pages: 328, Format: PDF

    except Exception as e:
        print(f"An error occurred: {e}")
