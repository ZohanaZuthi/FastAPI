from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Root path
@app.get('/')
def root():
    return {'name': 'Nazifa', 'age': 21}

# About path
@app.get('/about')
def about():
    return {'title': 'This is the about page'}

# Blog path with query parameters
@app.get('/blog')
def blog(limit: int = 9, unpublished: bool = True, sort: Optional[str] = None):
    if unpublished:
        return {'range': f'The limit is {limit}, unpublished is True'}
    else:
        return {'range': f'The limit is {limit}, unpublished is False'}

# Blog post with specific ID
@app.get('/blog/{id}')
def get_blog_by_id(id: int):
    return {'id': id}
