from fastapi import FastAPI
from pydantic import BaseModel


app=FastAPI()



@app.get('/about')
def myabout():
    return 'hello welcome to the team'
