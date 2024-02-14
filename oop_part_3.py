class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):

        return f"Title: {self.title}, Author: {self.author}" #f "formate"

    def __len__(self):
        return self.pages

mybook = Book("Python Rocks!", "jose", 250)
#print(mybook)
length_book = len(mybook)
print(length_book)
