# Library Management System

A simple, console-based Library Management System built with Python 3. This program allows users to add, issue, return, search, and view books, with preserving data storage using a local text file (`library.txt`).

## Features

* **Add Books:** Add new books with a title and author. Book IDs are automatically generated starting from `B101`.

* **Issue Books:** Issue available books to library members, prevent double-issuing, and display the remaining count of available books.

* **Return Books:** Return issued books and update their status back to `Available`.

* **Search Books:** Search the book by it’s title or author name.

* **View All Books:** Display a formatted list of all books currently in the library along with their availability status.

* **Preserving Storage:** Automatically loads saved records from `library.txt` on startup and saves all changes back to the file upon exiting.

## Concepts Used

* **Lists & Dictionaries:** Each book is represented as a dictionary (`id`, `title`, `author`, `status`) stored inside a list.

* **Functions:** Modular design with dedicated functions for each feature (`load_books`, `save_books`, `add_book`, `issue_book`, `return_book`, `search_book`, `display_books`).

* **File Handling:** Reading from and writing comma-separated records to `library.txt`.

## How to Run

1. Make sure Python 3 is installed on your computer.

2. Download the `Library Book Management.py` file.

3. Open it in any Python editor (like VS Code) and run it.

## Usage

When you run the program, you will see the following menu:

```
1. Add book
2. Issue book
3. Return book
4. Search book
5. View all books
6. Exit
Menu option:


```

> **Note:** Always select option **6 (Exit)** to ensure your changes are saved to `library.txt`.

## Test Cases

### Test Case 1: Normal Input

* **Input:**

  ```
  Menu option 1 (Add book)
  Title: Python Basics
  Author: Mark Lutz
  
  
  ```

* **Expected Output:**

  ```
  Book added. ID: B101 | Python Basics | Mark Lutz | Available
  
  
  ```

### Test Case 2: Boundary / Minimum Input

* **Input:**

  ```
  Library has only book B101
  Menu option 2 (Issue): ID B101, Member: Riya
  
  
  ```

* **Expected Output:**

  ```
  Book B101 issued to Riya. Status: Issued
  Available books: 0
  
  
  ```

### Test Case 3: Invalid Input

* **Input:**

  ```
  Menu option 2 (Issue)
  Book ID: B999
  
  
  ```

* **Expected Output:**

  ```
  Book ID B999 not found.
  
  
  ```

### Test Case 4: Different Valid Scenario

* **Input:**

  ```
  (a) Option 1: Data Science | Wes McKinney
  (b) Option 4 (Search by author): McKinney
  (c) Option 3 (Return): ID B101
  
  
  ```

* **Expected Output:**

  ```
  (a) Book added. ID: B102 | Data Science | Wes McKinney | Available
  (b) B102 | Data Science | Wes McKinney | Available
  (c) Book B101 returned. Status: Available
  
  
  ```

## Data Storage Format

Book records are stored in `library.txt` in the same directory as the script using a comma-separated format:

```
B101,Python Basics,Mark Lutz,Available,
B102,Data Science,Wes McKinney,Available,


```

## Project Structure

```
.
├── library.py      # Main Python program
├── library.txt     # Auto-generated data file for storing books
└── README.md       # Project documentation


```