from fastapi import FastAPI
from pydantic import BaseModel

class kiran(BaseModel):
    name:str
    email:str
    salary:int
    weight:float
    
app=FastAPI()



@app.get('/about')
def myabout():
    return 'hello welcome to the team'
