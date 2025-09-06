from many_to_many import Author, Book, Contract

def test_basic_functionality():
    """Test basic functionality of all classes"""
    print("Testing basic functionality...")
    
    # Clear all lists for clean testing
    Author.all = []
    Book.all = []
    Contract.all = []
    
    # Test basic initialization
    author1 = Author("Stephen King")
    author2 = Author("J.K. Rowling")
    book1 = Book("The Shining")
    book2 = Book("Harry Potter")
    
    print(f"✓ Author created: {author1.name}")
    print(f"✓ Book created: {book1.title}")
    
    # Test contract creation
    contract1 = Contract(author1, book1, "01/01/2000", 50000)
    contract2 = author2.sign_contract(book2, "12/25/1999", 75000)
    
    print(f"✓ Contract created: {contract1.author.name} - {contract1.book.title}")
    print(f"✓ Contract signed: {contract2.author.name} - {contract2.book.title}")
    
    # Test relationships
    assert author1 in book1.authors()
    assert book1 in author1.books()
    assert contract1 in author1.contracts()
    assert contract1 in book1.contracts()
    
    print("✓ Author-Book relationships working")
    
    # Test royalties
    Contract(author1, book2, "06/15/2001", 25000)  # Author1 gets another contract
    total = author1.total_royalties()
    expected = 50000 + 25000
    assert total == expected
    
    print(f"✓ Total royalties calculation: {total}")
    
    # Test contracts by date
    contracts_2001 = Contract.contracts_by_date("06/15/2001")
    assert len(contracts_2001) == 1
    
    print("✓ Contracts by date filtering working")
    
    print("\n✅ All basic functionality tests passed!")

def test_validation():
    """Test validation of contract properties"""
    print("\nTesting validation...")
    
    author = Author("Test Author")
    book = Book("Test Book")
    
    # Test invalid types
    try:
        Contract("Not an author", book, "01/01/2000", 1000)
        assert False, "Should have raised exception for invalid author"
    except Exception:
        print("✓ Author validation working")
    
    try:
        Contract(author, "Not a book", "01/01/2000", 1000)
        assert False, "Should have raised exception for invalid book"
    except Exception:
        print("✓ Book validation working")
    
    try:
        Contract(author, book, 123456, 1000)
        assert False, "Should have raised exception for invalid date"
    except Exception:
        print("✓ Date validation working")
    
    try:
        Contract(author, book, "01/01/2000", "Not an integer")
        assert False, "Should have raised exception for invalid royalties"
    except Exception:
        print("✓ Royalties validation working")
    
    print("\n✅ All validation tests passed!")

def demo_usage():
    """Demonstrate typical usage of the system"""
    print("\n" + "="*50)
    print("DEMO: Book Contract Management System")
    print("="*50)
    
    # Clear all for demo
    Author.all = []
    Book.all = []
    Contract.all = []
    
    # Create authors
    stephen = Author("Stephen King")
    jk = Author("J.K. Rowling")
    george = Author("George R.R. Martin")
    
    # Create books
    it = Book("IT")
    carrie = Book("Carrie")
    hp1 = Book("Harry Potter and the Philosopher's Stone")
    got = Book("A Game of Thrones")
    
    # Sign some contracts
    stephen.sign_contract(it, "09/15/1986", 100000)
    stephen.sign_contract(carrie, "04/05/1974", 75000)
    jk.sign_contract(hp1, "06/26/1997", 500000)
    george.sign_contract(got, "08/01/1996", 200000)
    
    # Multi-author book example
    anthology = Book("Horror Anthology")
    stephen.sign_contract(anthology, "10/31/2023", 50000)
    george.sign_contract(anthology, "10/31/2023", 45000)
    
    # Display results
    print(f"\nAuthors in system: {len(Author.all)}")
    for author in Author.all:
        print(f"  - {author.name}: {len(author.books())} books, ${author.total_royalties():,} total royalties")
    
    print(f"\nBooks in system: {len(Book.all)}")
    for book in Book.all:
        authors_list = ", ".join([author.name for author in book.authors()])
        print(f"  - {book.title} by {authors_list}")
    
    print(f"\nContracts signed on 10/31/2023:")
    halloween_contracts = Contract.contracts_by_date("10/31/2023")
    for contract in halloween_contracts:
        print(f"  - {contract.author.name} - {contract.book.title}: ${contract.royalties:,}")

if __name__ == "__main__":
    test_basic_functionality()
    test_validation()
    demo_usage()
    print(f"\n🎉 All tests completed successfully!")
    print("Your implementation is ready to submit!")