from fastapi import FastAPI

app = FastAPI()

def divide(a: int, b: int) -> float:
    return a / b

@app.get('/')
def division(a: int, b: int) -> float:
    return divide(a, b)
# to run manually
# This part will execute only if the script is run directly
if __name__ == '__main__':
    c = divide(10, 3)
    print(c)
