import json
from book import Book
from user import User

class Library:
    def __init__(self, data_file='data.json'):
        self.data_file = data_file
        self.books = {}
        self.users = {}
        self.load_data()

    def add_book(self, title, author, total_copies=1):
        book = Book(title, author, total_copies)
        self.books[book.book_id] = book
        self.save_data()
        print(f"Book '{title}' added successfully with {total_copies} copies.")

    def display_books(self):
        print("Books in Library:")
        for book in self.books.values():
            print(f"{book.title} by {book.author} - "
                  f"{book.available_copies}/{book.total_copies} available")

    def add_user(self, name):
        user = User(name)
        self.users[user.user_id] = user
        self.save_data()
        print(f"User '{name}' added successfully with ID {user.user_id}.")
    def borrow_book(self, user_id, book_id):
        if user_id not in self.users or book_id not in self.books:
            print("User or book not found.")
            return
        book = self.books[book_id]
        user = self.users[user_id]

        if book_id in user.borrowed_books:
            print(f"{user.name} has already borrowed '{book.title}'.")
            return

        if book.borrow():
            user.borrowed_books.append(book_id)
            self.save_data()
            print(f"Book '{book.title}' borrowed by {user.name}.")
        else:
            print(f"No copies of '{book.title}' are available.")


    def add_copies(self, book_id, additional_copies):
        if book_id not in self.books:
            print("Book not found.")
            return
        book = self.books[book_id]
        book.total_copies += additional_copies
        book.available_copies += additional_copies
        self.save_data()
        print(f"Added {additional_copies} copies to '{book.title}'. "
            f"Total copies: {book.total_copies}, Available: {book.available_copies}")
    def return_book(self, user_id, book_id):
        if user_id not in self.users or book_id not in self.books:
            print("User or book not found.")
            return
        book = self.books[book_id]
        user = self.users[user_id]

        if book_id not in user.borrowed_books:
            print(f"{user.name} did not borrow '{book.title}'.")
            return

        if book.return_book():
            user.borrowed_books.remove(book_id)
            self.save_data()
            print(f"Book '{book.title}' returned by {user.name}.")

    def save_data(self):
        data = {
            "books": {bid: b.to_dict() for bid, b in self.books.items()},
            "users": {uid: u.to_dict() for uid, u in self.users.items()}
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                for bid, b in data.get("books", {}).items():
                    book_obj = Book(
                        title=b['title'],
                        author=b['author'],
                        total_copies=b['total_copies'],
                        book_id=b['book_id']
                    )
                    book_obj.available_copies = b.get('available_copies', b['total_copies'])
                    self.books[bid] = book_obj

                for uid, u in data.get("users", {}).items():
                    user_obj = User(u['name'], u['user_id'])
                    user_obj.borrowed_books = u.get('borrowed_books', [])
                    self.users[uid] = user_obj
        except FileNotFoundError:
            self.books = {}
            self.users = {}
