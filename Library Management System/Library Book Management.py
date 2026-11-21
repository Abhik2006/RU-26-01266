books = []
def load_books():
  f = open("library.txt", "a")
  f.close()
  f = open("library.txt", "r")
  for line in f:
    data = line.split(",")
    if len(data) > 3:
      book = {
          "id": data[0],
          "title": data[1],
          "author": data[2],
          "status": data[3],
      }
      books.append(book)
  f.close()
def save_books():
  f = open("library.txt", "w")
  for b in books:
    f.write(
        b["id"] + "," + b["title"] + "," + b["author"] + "," + b["status"] + ",\n"
    )
  f.close()
def add_book():
  title = input("Title: ")
  author = input("Author: ")
  bid = "B" + str(101 + len(books))
  book = {"id": bid, "title": title, "author": author, "status": "Available"}
  books.append(book)
  print("Book added. ID:", bid, "|", title, "|", author, "| Available")
def issue_book():
  bid = input("Book ID: ")
  found = 0
  for b in books:
    if b["id"] == bid:
      found = 1
      if b["status"] == "Issued":
        print("Book is already issued.")
      else:
        member = input("Member: ")
        b["status"] = "Issued"
        print("Book", bid, "issued to", member + ". Status: Issued")
        avail = 0
        for x in books:
          if x["status"] == "Available":
            avail = avail + 1
        print("Available books:", avail)
  if found == 0:
    print("Book ID", bid, "not found.")
def return_book():
  bid = input("Book ID: ")
  found = 0
  for b in books:
    if b["id"] == bid:
      found = 1
      if b["status"] == "Available":
        print("Book is already available.")
      else:
        b["status"] = "Available"
        print("Book", bid, "returned. Status: Available")
  if found == 0:
    print("Book ID", bid, "not found.")
def search_book():
  text = input("Enter title or author to search: ")
  found = 0
  for b in books:
    if text in b["title"] or text in b["author"]:
      print(b["id"], "|", b["title"], "|", b["author"], "|", b["status"])
      found = 1
  if found == 0:
    print("Book not found.")
def display_books():
  if books == []:
    print("No books in library.")
  else:
    for b in books:
      print(b["id"], "|", b["title"], "|", b["author"], "|", b["status"])
load_books()
while True:
  print("\n1. Add book")
  print("2. Issue book")
  print("3. Return book")
  print("4. Search book")
  print("5. View all books")
  print("6. Exit")
  ch = input("Menu option: ")
  if ch == "1":
    add_book()
  elif ch == "2":
    issue_book()
  elif ch == "3":
    return_book()
  elif ch == "4":
    search_book()
  elif ch == "5":
    display_books()
  elif ch == "6":
    save_books()
    print("Data saved to library.txt. Exiting...")
    break
  else:
    print("Invalid option.")