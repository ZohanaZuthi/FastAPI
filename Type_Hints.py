# to get the division of two numbers
from fastapi import FastAPI
app=FastAPI()

@app.get('/')
def division(a:int,b:int)->float:
    return a/b
c=division(10,3)
print(c)
    