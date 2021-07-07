from fastapi import HTTPException,status,Depends
from .. import schemas,models
from sqlalchemy.orm import Session
from Blog.hashing import Hash
from ..database import get_db



def create(request:schemas.User,db:Session=Depends(get_db)):
    new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password),is_active=request.is_active)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id,db:Session=Depends(get_db)):
    user = db.query(models.User).get(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} is not available")
    return user