from fastapi import FastAPI , Depends , HTTPException
from sqlalchemy.orm import Session
from database.schema import UserCreate , UserUpdate 

from database.model import User
from database.session import get_db

app = FastAPI()

@app.get("/")
def home():
    return {
        "message" : "Welcome to MODELFORGE"
    }

@app.get("/health")
def health_check():
    return {
        "status" : "healthy",
        "service" : "ModelForge Backend"
    }
@app.post("/users")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    new_user = User(
        username=user.username,
        email=user.email
    )

    db.add(new_user)

    db.commit()

    return {
        "message": "User created successfully"
    }

@app.get("/users")
def get_users(
    db: Session = Depends(get_db)

):
    #users = db.query(User).all()
    users = db.query(User).filter(
    User.is_deleted == False
).all()
    return users

@app.get("/users/{user_id}")
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    # user = db.query(User).filter(
    #     User.id == user_id
    # ).first()
    user = db.query(User).filter(
    User.id == user_id,
    User.is_deleted == False
).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user
@app.put("/users/{user_id}")
def update_user(
    user_id: int,
    updated_user: UserUpdate,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.username = updated_user.username
    user.email = updated_user.email

    db.commit()

    return {
        "message": "User updated successfully"
    }

@app.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    # user = db.query(User).filter(
    #     User.id == user_id
    # ).first()
    user = db.query(User).filter(
    User.id == user_id,
    User.is_deleted == False
).first()
    
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # db.delete(user)

    # db.commit()
    user.is_deleted = True

    db.commit()



    return {
        "message": "User deleted successfully"
    }