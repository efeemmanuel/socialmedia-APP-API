
from .. import models, schemas, utils
from fastapi import FastAPI, status, HTTPException, Depends, APIRouter
from ..database import engine, get_db
from sqlalchemy.orm import Session



router = APIRouter(prefix="/users",
                   tags=['users'])



# user create

@router.post("/", response_model=schemas.UserOut)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # hash the passoerd
    hashed_password = utils.hash(user.password)  
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)   # Add the new post to the session
    db.commit()   # Save the post in the database
    db.refresh(new_user)   # Update the instance with the saved data

    return new_user



# get user
@router.get("/{id}", response_model=schemas.UserOut)
async def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return user

