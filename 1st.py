from fastapi import FastAPI

app=FastAPI()
# return multiple values as dictionary
@app.get('/')
def root():
    return {'name':'Nazifa', 'age':21}
# http://127.0.0.1:8000/about if i type this which is not dfined yet
# by default fastapi gives detail not found

#  now we are going to define about
@app.get('/about')
def about():
    return {'title':{'this is the about page'}}

 