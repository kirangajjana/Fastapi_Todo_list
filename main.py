from fastapi import FastAPI
from pydantic import BaseModel #pip install pydantic

class todo(BaseModel):
    marks:int
    age:int=200
    name:str
    state:str
    def task(self):
        self.marks=self.age+self.age
        return self.marks
    
         

app=FastAPI()



@app.get('/about')
def myabout():
    return 'hello welcome to the team'


@app.post('/home')
def homepage():
    return {f'hello world how are you'}

@app.post('/data')
def datastore(todo:todo):
    marks=todo.task()
    return {'marks':marks}