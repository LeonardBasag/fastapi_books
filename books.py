from fastapi import FastAPI, Body

app = FastAPI()

Books = [
    {'title': 'Title One ', 'author':'Author One', 'category':'science'},
    {'title': 'Title Two', 'author':'Author Two', 'category':'science'},
    {'title': 'Title Three', 'author':'Author Three', 'category':'history'},
    {'title': 'Title Four', 'author':'Author Four', 'category':'math'},
    {'title': 'Title Five', 'author':'Author Five', 'category':'math'},
    {'title': 'Title Six', 'author':'Author Two', 'category':'math'}
]

@app.get("/books")
async def get_books():
    return Books

@app.get("/books/{author}")
async def get_book_by_author(author: str):
    books_by_author = []
    for book in Books:
        if book.get('author').casefold() == author.casefold():
            books_by_author.append(book)
    return books_by_author

@app.get("/books/{book_title}")
async def get_book(book_title:str):
    for book in Books:
        if book.get('title').casefold() == book_title.casefold():
            return book
        
@app.get("/books/category/")
async def get_books_by_category(category:str):
    returned_books = []
    for book in Books:
        print(f'The category input {category}')
        print(book.get('category').casefold())
        print(category.casefold)
        if book.get('category').casefold() == category.casefold():
            returned_books.append(book)
    return returned_books

@app.post("/books/create-book")
async def create_book(new_book = Body()):
    Books.append(new_book)
    return new_book

@app.put("/books/update-book")
async def update_book(updated_book = Body()):
    for i in range(len(Books)):
        if Books[i].get('title').casefold() == updated_book.get('title').casefold():
            Books[i] = updated_book
            print(Books[i])
    return updated_book

@app.delete("/books/delete-book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(Books)):
        if Books[i].get('title').casefold() == book_title.casefold():
            Books.pop(i)
            break
    return book_title


