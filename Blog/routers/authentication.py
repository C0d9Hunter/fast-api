from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schemas,models,database,JWT_token
from ..hashing import Hash



router = APIRouter(tags=["Authentication"])
 
@router.post("/login")
def login(request:OAuth2PasswordRequestForm = Depends(),db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalide credentials")

    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"password incorrect") 

    access_token = JWT_token.create_access_token(data={"sub": request.username})
    return {"access_token": access_token, "token_type": "bearer"}