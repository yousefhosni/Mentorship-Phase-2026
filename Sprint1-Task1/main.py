from InquirerPy import inquirer
from library import Library

def main():
    lib = Library()

    while True:
        choice = inquirer.select(
            message="Select an action",
            choices=[
                'Add Book',
                'Add User',
                'Borrow Book',
                'Return Book',
                'Add Copies',
                'Display Books',
                'Exit'
            ]
        ).execute()

        # ------------------- ADD BOOK -------------------
        if choice == 'Add Book':
            title = inquirer.text(message="Enter Book Title").execute()
            author = inquirer.text(message="Enter Author Name").execute()
            total_copies = int(inquirer.text(
                message="Enter Number of Copies",
                default="1"
            ).execute())
            lib.add_book(title, author, total_copies)

        # ------------------- ADD USER -------------------
        elif choice == 'Add User':
            name = inquirer.text(message="Enter User Name").execute()
            lib.add_user(name)

        # ------------------- BORROW BOOK -------------------
        elif choice == 'Borrow Book':
            if not lib.users or not lib.books:
                print("No users or books available.")
                continue

            # Select User
            user_name = inquirer.fuzzy(
                message="Select User",
                choices=[u.name for u in lib.users.values()]
            ).execute()
            user_obj = next(u for u in lib.users.values() if u.name == user_name)

            # Select Book (only show books with copies and not already borrowed by user)
            available_books = [
                f"{b.title} by {b.author} ({b.available_copies}/{b.total_copies} available)"
                for b in lib.books.values()
                if b.is_available() and b.book_id not in user_obj.borrowed_books
            ]
            if not available_books:
                print("No books available to borrow for this user.")
                continue

            book_choice = inquirer.fuzzy(
                message="Select Book to Borrow",
                choices=available_books
            ).execute()
            # Extract book object
            book_title = book_choice.split(" by ")[0]
            book_obj = next(b for b in lib.books.values() if b.title == book_title)

            lib.borrow_book(user_obj.user_id, book_obj.book_id)

        # ------------------- RETURN BOOK -------------------
        elif choice == 'Return Book':
            # Users with borrowed books
            users_with_borrowed = [u for u in lib.users.values() if u.borrowed_books]
            if not users_with_borrowed:
                print("No borrowed books.")
                continue

            # Select User
            user_name = inquirer.fuzzy(
                message="Select User",
                choices=[u.name for u in users_with_borrowed]
            ).execute()
            user_obj = next(u for u in lib.users.values() if u.name == user_name)

            # Select Book to return
            book_choices = [
                f"{lib.books[b].title} by {lib.books[b].author}" 
                for b in user_obj.borrowed_books
            ]
            book_choice = inquirer.fuzzy(
                message="Select Book to Return",
                choices=book_choices
            ).execute()
            book_title = book_choice.split(" by ")[0]
            book_obj = next(b for b in lib.books.values() if b.title == book_title)

            lib.return_book(user_obj.user_id, book_obj.book_id)

        # ------------------- ADD COPIES -------------------
        elif choice == 'Add Copies':
            if not lib.books:
                print("No books available.")
                continue

            book_choice = inquirer.fuzzy(
                message="Select Book to Add Copies",
                choices=[f"{b.title} by {b.author}" for b in lib.books.values()]
            ).execute()
            book_title = book_choice.split(" by ")[0]
            book_obj = next(b for b in lib.books.values() if b.title == book_title)

            additional_copies = int(inquirer.text(
                message="Enter number of additional copies",
                default="1"
            ).execute())

            lib.add_copies(book_obj.book_id, additional_copies)

        # ------------------- DISPLAY BOOKS -------------------
        elif choice == 'Display Books':
            lib.display_books()

        # ------------------- EXIT -------------------
        elif choice == 'Exit':
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
