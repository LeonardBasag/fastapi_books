from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status

app = FastAPI()

class Book:
    id:int
    title:str
    author:str
    description:str
    published_date: int
    rating:int

    def __init__(self, id, title, author, description, published_date, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.published_date=published_date
        self.rating = rating

class Book_Request(BaseModel):
    id:Optional[int] = Field(description='ID is not needed on create', default=None)
    title:str = Field(min_length=3)
    author:str = Field(min_length=3)
    description:str = Field(min_length=3, max_length=100)
    published_date:int = Field(gt=1990, lt=2031)
    rating:int = Field(gt=-1, lt=6)

    model_config = {
        "json_schema_extra": {
            'example':{
                'title': 'A new book',
                'author':'codingwithroby',
                'description': 'Add a description for this book',
                'published_date':'The year the book was published',
                'rating': 5
            }
        }
    }


Books = [
    Book(1, 'Computer Science Pro', 'codinwithroby', 'A very nice book', 2020, 5),
    Book(2, 'Be fast with Fastapi', 'codinwithroby', 'A great book', 2023, 5),
    Book(3, 'Master endpoints', 'codinwithroby', 'A awesome book', 1999, 5),
    Book(4, 'HP1', 'Author 1', 'Book description', 2014, 3),
    Book(5, 'HP2', 'Author 2', 'Book description', 2020, 2),
    Book(6, 'HP3', 'Author 3', 'Book description', 2023, 1),

]

@app.get("/books", status_code=status.HTTP_200_OK)
async def get_all_books():
    return Books

@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: Book_Request):
    new_book = Book(**book_request.model_dump())
    Books.append(find_book_id(new_book))
    return new_book

@app.get("/books/{book_id}")
async def get_book_by_id(book_id:int = Path(gt=0)):
    print("You are in get by id")
    for book in Books:
        if book_id == book.id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')
        
@app.get("/books/", status_code=status.HTTP_200_OK)
async def get_book_by_rating(rating:int = Query(gt=0, lt=6)):
    books_to_return =[]
    for book in Books:
        if book.rating == rating:
            books_to_return.append(book)
    return books_to_return

@app.put("/books/update-book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: Book_Request):
    book_changed = False
    for i in range(len(Books)):
        if Books[i].id == book.id:
            Books[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item to update not found')

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int = Path(gt=0)):
    book_changed = False
    for i in range(len(Books)):
        if Books[i].id == book_id:
            Books.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item to delete not found")

@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def get_book_by_published_date(published_date: int = Query(gt=1999, lt=2031)):
    print("You are in get by published date")
    books_to_return = []
    for book in Books:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return
 




def find_book_id(book:Book):
    # if len(Books) > 0:
    #     book.id = Books[-1].id + 1
    # else:
    #     book.id = 1

    book.id = 1 if len(Books) == 0 else Books[-1].id + 1
    return book
