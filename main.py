from fastapi import FastAPI
from  typing import Optional
from pydantic import BaseModel
from starlette.routing import Host
import uvicorn

class Blog(BaseModel):
    title:str
    body: str
    published:Optional[bool]
    comments: Optional[list]=[]
     

app = FastAPI()

@app.get("/blog")
def index(limit:int = 10,published:bool = True, sort:Optional[str] = None):
    if published:
        return {"data":f"{limit} published blogs of DB"}
    else:
        return {"data":f"{limit} blogs of DB"}

@app.get("/blog/unpublished")
def unpublished():
    return {"data":"All unpublished blogs"}

@app.get("/blog/{id}")
def show(id:int):
    return {"data":id}

@app.get("/blog/{id}/comments")
def comments(id:int,limit=10):
    return {"data":['1','2']}

@app.post("/blog")
def create_blog(blog :Blog):
    return {"data":f"Blog has been created with title:{blog.title}, body:{blog.body}, comments:{len(blog.comments)}"}


# if __name__=="__main__":
#     uvicorn.run(app,host="127.0.0.1",port=9000)