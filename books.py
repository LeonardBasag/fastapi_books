from fastapi import FastAPI

app = FastAPI()

Books = [
    {'title': 'Title One ', 'author':'Author One', 'category':'science'},
    {'title': 'Title Two', 'author':'Author Two', 'category':'science'},
    {'title': 'Title Three', 'author':'Author Three', 'category':'history'},
    {'title': 'Title Four', 'author':'Author Four', 'category':'math'},
    {'title': 'Title Five', 'author':'Author Five', 'categor':'math'},
    {'title': 'Title Six', 'author':'Author Two', 'category':'math'}
]

@app.get("/books")
async def get_books():
    return Books

@app.get("/books/{book_title}")
async def get_book(book_title:str):
    for book in Books:
        if book.get('title').casefold() == book_title.casefold():
            return book