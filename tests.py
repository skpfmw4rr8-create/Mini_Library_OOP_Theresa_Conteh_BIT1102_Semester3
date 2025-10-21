# tests.py
from operations import *

# Reset Data
books.clear()
members.clear()

# Test 1: Add Book
assert add_book("111", "Book A", "Author A", "Fiction", 2) == "Book 'Book A' added successfully."

# Test 2: Add Member
assert add_member("M001", "John Doe", "john@mail.com") == "Member 'John Doe' added successfully."

# Test 3: Borrow Book
borrow_msg = borrow_book("M001", "111")
assert "borrowed" in borrow_msg

# Test 4: Return Book
return_msg = return_book("M001", "111")
assert "returned" in return_msg

# Test 5: Prevent Over-Borrowing
add_book("112", "Book B", "Author B", "Fiction", 1)
borrow_book("M001", "111")
borrow_book("M001", "112")
add_book("113", "Book C", "Author C", "Fiction", 1)
add_book("114", "Book D", "Author D", "Fiction", 1)
borrow_book("M001", "113")
assert "limit" in borrow_book("M001", "114")

print("✅ All tests passed successfully!")
