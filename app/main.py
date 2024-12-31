from fastapi import FastAPI, status, HTTPException, Depends
# from fastapi.params import Body 
# from typing import Optional, Lis



from fastapi.middleware.cors import CORSMiddleware


from . import models
from .database import engine, get_db
# from . import schemas, utils
from .router import post,user, auth, vote


# instance of the class
from .config import settings   
# ensures that your database schema (tables) is created based on your SQLAlchemy models
# this is not needed again becuaase it is to tell sqlalchemy to generate the table when we first started out
# models.Base.metadata.create_all(bind=engine)



# from sqlalchemy.orm import Session

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)








app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "Welcome to my API"}





















































# FOR PSYCOPG USING RAW SQL

# # our schema   when using psycopg2 i guess 
# class posts(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     # rating: Optional[int] = None




# # when using psycopg2 to connect app and postgress using raw SQL 
# while True:

#     try:
#         conn = psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='testing123', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("DB connection was a success")
#         break
#     except Exception as error:
#         print("was not successful")
#         print('Error:, ', error)
#         time.sleep(2)



# @app.get("/")
# async def root():
#     return {"message": "Welcome to my API"}


# @app.get("/posts")
# async def get_post():
#     cursor.execute(""" SELECT * FROM "Post" """)
#     posts = cursor.fetchall()
#     return{"data": posts}

# @app.post("/posts")
# async def create_posts(post:posts):
#     cursor.execute(""" INSERT INTO "Post" (title, content, published) VALUES(%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
#     new_posts = cursor.fetchone()

#     conn.commit()
#     return {"data":new_posts}




# @app.get("/posts/{id}")
# async def get_posts(id: int):
#     cursor.execute("""SELECT * FROM "Post" WHERE id = %s""", (id,))  # Correctly pass as a tuple
#     post = cursor.fetchone()

#     if not post:
#         raise HTTPException(status_code=404, detail="Post not found")

#     return {"data": post}




# @app.put("/posts/{id}")
# async def update_posts(id: int, post:posts):
#     cursor.execute("""UPDATE "Post" SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """, (post.title, post.content, post.published, (str(id))))
#     updated_post = cursor.fetchone()

#     if not updated_post:
#         raise HTTPException(status_code=404, detail="Post not found")

#     conn.commit()
#     return {"data": updated_post}






# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_post(id:int):
#     cursor.execute(""" DELETE FROM "Post" WHERE id = %s returning * """, (str(id),))
#     delete_posts=cursor.fetchone()

#     if delete_posts == None:
#         raise HTTPException(status_code=404, detail="Post not found")

#     conn.commit()
#     return {"data":delete_posts}



























































# VERY BEGINEER LEVEL


# my_posts = [{"title": "titleof post 1", "content":"content of post 1", "id": 1}, {"title": "favourite food", "content":"i love pizza", "id": 2}]


# @app.get("/")
# async def root():
#     return {"message": "Welcome to my API"}


# @app.get("/posts")
# async def get_post():
#     cursor.execute(""" SELECT * FROM posts """)
#     posts = cursor.fetchall()
#     return{"data": my_posts}

# @app.post("/posts")
# async def create_posts(post:Post):
#     # print(post)
#     # print(post.dict())
#     my_posts.append()
#     return {"data":post}

# @app.get("/posts/{id}")
# async def get_post(id:int):
#     return {"data": f"this is the {id}"}



# @app.delete("/posts/{id}")
# async def delete_post(id:int):
#     if my_posts["id"] in my_posts:
#         my_posts.remove(id)
#     return {"data":"post has been deleted"}


# @app.post("/createposts")
# async def create_posts(payload: dict = Body(...)):
#     return {"new_post":f"title{payload['title']} content{payload['content']}"}


# a schema is to describe what te data we are getting should ook like 




