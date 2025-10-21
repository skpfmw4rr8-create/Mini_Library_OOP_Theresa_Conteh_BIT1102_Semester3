# operations.py
"""
Mini Library Management System
Author: Bah
Date: October 2025

This module implements the core operations for a library management system using:
- Dictionary for books (ISBN as key)
- List of dictionaries for members
- Tuple for genres
"""

# -----------------------------
# DATA STRUCTURES
# -----------------------------

genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Biography", "Mystery", "Fantasy")

# ISBN: {title, author, genre, total_copies, available_copies}
books = {}

# Members: list of dicts
members = []


# -----------------------------
# HELPER FUNCTIONS
# -----------------------------

def find_member(member_id):
    """Return member dictionary by ID."""
    for member in members:
        if member["member_id"] == member_id:
            return member
    return None


# -----------------------------
# CORE FUNCTIONS
# -----------------------------

def add_book(isbn, title, author, genre, total_copies):
    """Add a new book to the system if ISBN is unique and genre is valid."""
    if isbn in books:
        return "Error: ISBN already exists."
    if genre not in genres:
        return "Error: Invalid genre."
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies,
        "available_copies": total_copies
    }
    return f"Book '{title}' added successfully."


def add_member(member_id, name, email):
    """Add a new member if ID is unique."""
    if find_member(member_id):
        return "Error: Member ID already exists."
    members.append({
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    })
    return f"Member '{name}' added successfully."


def search_books(keyword):
    """Search for books by title or author (case-insensitive)."""
    keyword = keyword.lower()
    results = [
        {"ISBN": isbn, **details}
        for isbn, details in books.items()
        if keyword in details["title"].lower() or keyword in details["author"].lower()
    ]
    return results if results else "No books found."


def update_book(isbn, **kwargs):
    """Update book details."""
    if isbn not in books:
        return "Error: Book not found."
    books[isbn].update(kwargs)
    return f"Book '{books[isbn]['title']}' updated successfully."


def update_member(member_id, **kwargs):
    """Update member details."""
    member = find_member(member_id)
    if not member:
        return "Error: Member not found."
    member.update(kwargs)
    return f"Member '{member['name']}' updated successfully."


def delete_book(isbn):
    """Delete a book if no copies are borrowed."""
    if isbn not in books:
        return "Error: Book not found."
    if books[isbn]["available_copies"] != books[isbn]["total_copies"]:
        return "Error: Cannot delete book with borrowed copies."
    del books[isbn]
    return f"Book with ISBN {isbn} deleted successfully."


def delete_member(member_id):
    """Delete a member if they have no borrowed books."""
    member = find_member(member_id)
    if not member:
        return "Error: Member not found."
    if member["borrowed_books"]:
        return "Error: Cannot delete member with borrowed books."
    members.remove(member)
    return f"Member '{member['name']}' deleted successfully."


def borrow_book(member_id, isbn):
    """Allow member to borrow a book if copies are available (max 3)."""
    member = find_member(member_id)
    if not member:
        return "Error: Member not found."
    if isbn not in books:
        return "Error: Book not found."
    if books[isbn]["available_copies"] <= 0:
        return "Error: No copies available."
    if len(member["borrowed_books"]) >= 3:
        return "Error: Borrow limit reached."

    books[isbn]["available_copies"] -= 1
    member["borrowed_books"].append(isbn)
    return f"Book '{books[isbn]['title']}' borrowed by {member['name']}."


def return_book(member_id, isbn):
    """Allow member to return a borrowed book."""
    member = find_member(member_id)
    if not member:
        return "Error: Member not found."
    if isbn not in member["borrowed_books"]:
        return "Error: This book was not borrowed by member."

    member["borrowed_books"].remove(isbn)
    books[isbn]["available_copies"] += 1
    return f"Book '{books[isbn]['title']}' returned by {member['name']}."

