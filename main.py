from fastapi import FastAPI

app = FastAPI()

@app.get("/") # path operation decorator
def read_root():
    return {"message":"Hello World from FASTAPI"}

# POST,PUT,DELETE ,GET

@app.get("/demo") # path operation decorator
def demo_func():
    return {"message":"This is output from demo function"}

@app.post("/post_demo") # path operation decorator
def demo_post():
    return {"message":"This is output from post demo function"}

@app.get('/hello/{name}')
async def hello(name):
    return f'welcome to fastapi tutorial {name}'

