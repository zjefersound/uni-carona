from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def read_ride():
    return {"message": "Hello!"}
