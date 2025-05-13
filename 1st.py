from fastapi import FastAPI

app=FastAPI()
# return multiple values as dictionary
@app.get('/')
def root():
    return {'name':'Nazifa', 'age':21}
# http://127.0.0.1:8000/about if i type this which is not dfined yet
# by default fastapi gives detail not found

#  now we are going to define about
# @app is the path operator decorator 
# here operator path
@app.get('/about')
# path operation function
def about():
    return {'title':{'this is the about page'}}

@app.get('/blog')
def blog(limit):
    return {'range':f'the limit is {limit}'}
# run http://127.0.0.1:8000/blog?limit=5
@app.get('/blog/{id}')
def id(id:int):
    #  if we dont put int that will be string
    # fetching blog with id
    return {'id':{id}}
# go to http://127.0.0.1:8000/docs to see all the path that have been created
#  got to http://127.0.0.1:8000/redoc to check all the path as web


#  to run and reload uvicorn app:app --reload
