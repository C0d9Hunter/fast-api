from pydantic import BaseModel
from typing import Optional,List

class Blog(BaseModel):
    title:str 
    body:str
    published:Optional[bool]=False
    
    class Config():
        orm_mode = True



class User(BaseModel):
    name:str 
    email:str
    password:str
    is_active:Optional[bool]=True

class ShowUser(BaseModel):
    name:str 
    email:str
    blogs: List[Blog] = []
    
    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title:str 
    body:str 
    owner: ShowUser

    class Config():
        orm_mode = True

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None