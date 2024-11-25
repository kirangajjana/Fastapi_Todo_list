from fastapi import FastAPI

app=FastAPI()



@app.get('/about')
def myabout():
    return 'hello welcome to the team'
