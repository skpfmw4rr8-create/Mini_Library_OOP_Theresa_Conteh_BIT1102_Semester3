# demo.py
from operations import *

print("\n=== Library Management System Demo ===")

# Add Books
print(add_book("978-1", "1984", "George Orwell", "Fiction", 4))
print(add_book("978-2", "A Brief History of Time", "Stephen Hawking", "Non-Fiction", 2))
print(add_book("978-3", "Dune", "Frank Herbert", "Sci-Fi", 3))

# Add Members
print(add_member("M001", "Alice Johnson", "alice@mail.com"))
print(add_member("M002", "Bob Smith", "bob@mail.com"))

# Search Books
print("\nSearch results for 'dune':", search_books("dune"))

# Borrow Books
print(borrow_book("M001", "978-1"))
print(borrow_book("M001", "978-3"))
print(borrow_book("M002", "978-2"))

# Try to Borrow Beyond Limit
print(borrow_book("M001", "978-2"))

# Return Book
print(return_book("M001", "978-1"))

# Delete Member (should fail if they have borrowed books)
print(delete_member("M002"))

# Update Book
print(update_book("978-3", total_copies=5))

# Delete Book
print(delete_book("978-1"))

print("\n=== Demo Complete ===")
