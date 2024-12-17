from .. import models, schemas
from fastapi import FastAPI, status, HTTPException, Depends, APIRouter, Response
from ..database import engine, get_db
from sqlalchemy.orm import Session
from typing import Optional, List
from .. import oauth2

from sqlalchemy import func
 


router =APIRouter(prefix="/posts",
                  tags=['posts'])

# }/posts?limit=8

@router.get("/", response_model=List[schemas.PostOut])
async def get_post(db:Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user),
                   limit: int = 10, search: Optional[str] = ""):
    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).all()

    # results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id  == models.Post.id, isouter=True).group_by(models.Post.id).all()

    # return results
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).all()
    return posts

# @router.get("/", response_model=List[schemas.Post])
# async def get_post(db:Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
#     posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()
#     return posts
# #




# @router.post("/", response_model=schemas.Post)
# async def create_posts(post: schemas.PostCreate, db:Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
    
#     # new_posts = models.Post(title=post.title, content = post.content, published=post.published)
#     new_posts = models.Post(owner_id =get_current_user.id ,**post.dict())
#     db.add(new_posts)   # Add the new post to the session
#     db.commit()   # Save the post in the database
#     db.refresh(new_posts)   # Update the instance with the saved data
#     return new_posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):


    new_post = models.Post(owner_id=get_current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post









@router.get("/{id}", response_model=schemas.PostOut)
async def get_posts(id: int, db:Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
    
    # post = db.query(models.Post).filter(models.Post.id==id).first()
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()


    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return post




@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    # cursor.execute(
    #     """DELETE FROM posts WHERE id = %s returning *""", (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


#
# @app.put("/posts/{id}")
# async def update_posts(id: int, post:Post,  db:Session = Depends(get_db)):
#     query_post = db.query(models.Post).filter(models.Post.id==id)
#     post = query_post.first()

#     if post == None:
#         raise HTTPException(status_code=404, detail="Post not found")
    
#     query_post.update(post.dict(), synchronize_session=False)

#     conn.commit()
#     return {"data": query_post.first()}


# From chatgpt
# @router.put("/{id}", response_model=schemas.Post)
# async def update_posts(id: int, post: schemas.PostCreate, db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
#     query_post = db.query(models.Post).filter(models.Post.id == id)
#     existing_post = query_post.first()

#     if existing_post is None:
#         raise HTTPException(status_code=404, detail="Post not found")
    
#     if existing_post.owner_id != current_user.id:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perfrom operation")
    
#     query_post.update(post.dict(), synchronize_session=False)
#     db.commit()
#     db.refresh(existing_post)  # Refresh to reflect updated data
    
#     return {"data": existing_post}

  

@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
    #                (post.title, post.content, post.published, str(id)))

    # updated_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    post_query.update(updated_post.dict(), synchronize_session=False)

    db.commit()

    return post_query.first()

    # return post_query.first()
