from fastapi import HTTPException,status,Depends
from sqlalchemy.orm import Session
from .. import models,schemas
from ..database import get_db

def get_all(db:Session=Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request:schemas.Blog, current_user:schemas.User, db:Session=Depends(get_db)):
    new_blog = models.Blog(title=request.title,body=request.body,published=request.published,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id,db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return f"Blog deleted successfully!"
    
    
def update(id,request:schemas.Blog,db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog id: {id} not found")
    
    blog.update({"title":request.title,"body":request.body,"published":request.published}, synchronize_session=False)
    db.commit()
    return "Blog updated!"


def show(id, db:Session=Depends(get_db)):
    blog = db.query(models.Blog).get(id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available")
              
    return blog



