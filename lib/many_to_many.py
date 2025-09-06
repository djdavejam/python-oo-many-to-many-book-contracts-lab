class Author:
    """Author class representing book authors"""
    all = []
    
    def __init__(self, name):
        """Initialize author with name"""
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        """Return list of contracts associated with this author"""
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        """Return list of books associated with this author through contracts"""
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        """Create and return a new contract between author and book"""
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        """Return total royalties earned from all contracts"""
        return sum(contract.royalties for contract in self.contracts())


class Book:
    """Book class representing published books"""
    all = []
    
    def __init__(self, title):
        """Initialize book with title"""
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        """Return list of contracts associated with this book"""
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        """Return list of authors associated with this book through contracts"""
        return [contract.author for contract in self.contracts()]


class Contract:
    """Contract class representing agreements between authors and books"""
    all = []
    
    def __init__(self, author, book, date, royalties):
        """Initialize contract with author, book, date, and royalties"""
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @property
    def author(self):
        """Get the author of this contract"""
        return self._author
    
    @author.setter
    def author(self, value):
        """Set the author, validating it's an Author instance"""
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author class")
        self._author = value
    
    @property
    def book(self):
        """Get the book of this contract"""
        return self._book
    
    @book.setter
    def book(self, value):
        """Set the book, validating it's a Book instance"""
        if not isinstance(value, Book):
            raise Exception("Book must be an instance of Book class")
        self._book = value
    
    @property
    def date(self):
        """Get the date of this contract"""
        return self._date
    
    @date.setter
    def date(self, value):
        """Set the date, validating it's a string"""
        if not isinstance(value, str):
            raise Exception("Date must be a string")
        self._date = value
    
    @property
    def royalties(self):
        """Get the royalties of this contract"""
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        """Set the royalties, validating it's an integer"""
        if not isinstance(value, int):
            raise Exception("Royalties must be an integer")
        self._royalties = value
    
    @classmethod
    def contracts_by_date(cls, target_date):
        """Return all contracts with the specified date"""
        return [contract for contract in cls.all if contract.date == target_date]