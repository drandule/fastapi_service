from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {'status' : True}

@app.get("/helth")
def helth():
    return {'status' : 'unknown'}