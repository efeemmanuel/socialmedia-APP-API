from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional



from pydantic import conint



# FOR USERS
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True 


class UserLogin(BaseModel):
    email:EmailStr
    password: str



# this is for pydantic shema
# FOR POSTS
# FOR REQUEST
# our schema   when using psycopg2/ pydantic model i guess    , provides validation for our create post from the frontend, it is not reallly needed
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating: Optional[int] = None

class PostCreate(PostBase):
    pass



# FOR RESPOND
class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True 



# FOR TOKEN
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int





class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

class PostOut(BaseModel):
    Post: Post
    votes: int