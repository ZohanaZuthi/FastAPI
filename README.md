This project is based on the tutorial from [TutorialsPoint - FastAPI OpenAPI](https://www.tutorialspoint.com/fastapi/fastapi_openapi.htm).  
It demonstrates how FastAPI automatically generates interactive API documentation using **OpenAPI** and **Swagger UI**.

## 🔍 What is FastAPI?

**FastAPI** is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.  
It is built on top of **Starlette** for web handling and **Pydantic** for data validation.  

Key features include:
- Fast development with automatic generation of documentation
- Built-in validation and serialization
- Interactive API docs via Swagger UI
- High performance, comparable to Node.js and Go

Official site: [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com)

## 📦 How to Run

1. Install FastAPI and Uvicorn (if not already installed):
   ```bash
   pip install fastapi uvicorn
````

2. Run the FastAPI app:

   ```bash
   uvicorn main:app --reload
   ```

   Replace `main` with your Python filename if it's different (without `.py`).

## 📚 Interactive API Documentation

After starting the server, open your browser and go to:

```
http://127.0.0.1:8000/docs
```

This opens the **Swagger UI** – an interactive interface where you can:

* Explore all API endpoints
* Read descriptions and see expected input/output
* Try out API requests directly from the browser

You can also access the raw OpenAPI schema at:

```
http://127.0.0.1:8000/openapi.json
```
