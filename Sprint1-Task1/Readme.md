# Library Management System (Python OOP)

A console-based Library Management System implemented in Python using Object-Oriented Programming (OOP) and JSON as a simple database. The system allows adding books and users, borrowing and returning books, managing multiple copies of books, and interactively selecting books and users with fuzzy search using InquirerPy.

## Features

- Add Book: Add a new book with title, author, and number of copies.
- Add User: Add a new user (ID is auto-generated).
- Borrow Book: Borrow available books. A user can only borrow each book once. Fuzzy search makes selection easy.
- Return Book: Return previously borrowed books. Fuzzy search simplifies selection.
- Add Copies: Increase the number of copies for an existing book.
- Display Books: List all books with total and available copies.
- Data Persistence: All data is saved to data.json and loaded automatically.
- Interactive Menu: Uses InquirerPy for a clean, menu-driven console interface.

## Requirements

Python 3.7+

Packages:

- InquirerPy (for interactive menus and fuzzy search)

Install dependencies:
```sh
pip install inquirer
pip install InquirerPy
```

## Project Structure
lib_system/
│
├── main.py          # Main program with interactive menu
├── library.py       # Library class handling books, users, borrowing, and returning
├── book.py          # Book class with multiple copies support
├── user.py          # User class with borrowed books tracking
└── data.json        # JSON database storing books and users

## How to Run

Clone the repository or copy the project folder.

Ensure Python and InquirerPy are installed.

Run the program:

```sh
python main.py
```

Use the arrow keys to navigate the menu and Enter to select options.

Usage
Add Book

Enter book title, author, and number of copies.

Add User

Enter the user’s name. ID is generated automatically.

Borrow Book

Select a user (fuzzy search).

Select a book (fuzzy search). Only available books not already borrowed by the user are shown.

Return Book

Select a user who has borrowed books.

Select a book to return from their borrowed list.

Add Copies

Select a book (fuzzy search).

Enter the number of additional copies to add.

Display Books

Shows all books with the format:

Title by Author - Available Copies / Total Copies
