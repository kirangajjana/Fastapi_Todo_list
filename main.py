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
@app.get('/contact/{name}') #path parameter
def nameer(name:str):
    return {'name':name}

food_items={
    'northindian':['biriyani','mutton','chicken'],
    'southindian':['thalli','dhonne biriyani','chicken biriyani','mutton_biriyani'],
    'bihari':['mutton','chicken','litti choka','mashroom']
}

@app.get('/view/')
def viewer(marks1:int=21,marks2:int=25):
    return {'marks':marks1+marks2}
@app.get('/hotel/{cusine}')
def hotelwork(cusine):
    return food_items.get(cusine)