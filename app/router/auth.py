from fastapi import APIRouter, Depends,status, HTTPException, Response
from sqlalchemy.orm import Session

# from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from .. import database, schemas, models, utils, oauth2

router=APIRouter(tags=['Authentication'])


@router.post('/login', response_model=schemas.Token)
async def login(user_credentials: schemas.UserLogin ,db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN) 
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN) 
    
    access_token = oauth2.create_access_token(data = {"user_id":user.id})
    
    return {"access_token" : access_token,"token_type":"bearer"}
    
    
