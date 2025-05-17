# The first step in creating a FastAPI app is to declare the application object of FastAPI class.
from fastapi import FastAPI
app=FastAPI()
# The next step is to create path operation
# the index() function corresponds to / path with get operation.
@app.get('/')
def index():
    return{"msg":"Hello World"}
# The function returns a JSON response, however, it can return dict, list, str, int, etc. It can also return Pydantic models.
# FastAPI generates a schema using OpenAPI specifications
# The specification determines how to define API paths, path parameters, etc. The API schema defined by the OpenAPI standard decides how the data is sent using JSON Schema. 
# Visit http://127.0.0.1:8000/openapi.json from your browser. 

# Enter the following URL in the browser to generate automatically the interactive documentation.
# http://127.0.0.1:8000/docs