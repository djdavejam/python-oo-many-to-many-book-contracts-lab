# Book Contract Management System

A Python implementation of a many-to-many relationship between Authors, Books, and Contracts.

## Overview

This system manages publishing contracts where:
- Authors can write multiple books
- Books can have multiple authors  
- Contracts connect authors to books with date and royalty information

## Classes

### Author
```python
author = Author("Stephen King")
```
- **Methods:**
  - `contracts()` - Get all contracts for this author
  - `books()` - Get all books by this author
  - `sign_contract(book, date, royalties)` - Create new contract
  - `total_royalties()` - Sum of all earned royalties

### Book
```python
book = Book("The Shining")
```
- **Methods:**
  - `contracts()` - Get all contracts for this book
  - `authors()` - Get all authors of this book

### Contract
```python
contract = Contract(author, book, "01/01/2000", 50000)
```
- **Properties:** author, book, date, royalties (all validated)
- **Class Method:** `contracts_by_date(date)` - Find contracts by date

## Quick Example

```python
from many_to_many import Author, Book, Contract

# Create author and book
stephen = Author("Stephen King")
it_book = Book("IT")

# Sign contract
contract = stephen.sign_contract(it_book, "09/15/1986", 100000)

# Check relationships
print(stephen.books())        # [IT]
print(it_book.authors())      # [Stephen King]
print(stephen.total_royalties())  # 100000
```

## Running Tests

```bash
# Run all tests
python -m pytest

# Or use the test runner
python test_runner.py
```

## Features

✅ **Many-to-many relationships** between Authors and Books  
✅ **Data validation** for all contract properties  
✅ **Automatic tracking** of all instances  
✅ **Royalty calculations** and date filtering  
✅ **Comprehensive test suite**
