from fastapi import FastAPI

app = FastAPI()

Books = [
    {'title': 'Title1', 'author':'Author1', 'pages':'397'},
    {'title': 'Title2', 'author':'Author2', 'pages':'230'},
    {'title': 'Title3', 'author':'Author3', 'pages':'490'},
    {'title': 'Title4', 'author':'Author4', 'pages':'210'},
    {'title': 'Title5', 'author':'Author5', 'pages':'453'},
]

@app.get("/books")
async def get_books():
    return Books

@app.get("/books/{book_title}")
async def get_book(book_title:str):
    for book in Books:
        if book.get('title').casefold() == book_title.casefold():
            return book