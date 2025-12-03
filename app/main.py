from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()


# Creating Dependency Function
async def common_parameters(q:str | None =None , skip: int = 0, limit: int = 100):
  return {"q": q, "skip": skip, "limit": limit}


# Using Dependency in endpoints

@app.get("/items")
# defined parameters of route function main likhna Depends() main 
async def get_items(commons: Annotated[dict, Depends(common_parameters)]):
  return commons


@app.get("/users")
# defined parameters of route function main likhna Depends() main 
async def get_users(commons: Annotated[dict, Depends(common_parameters)]):
  return commons


# Create a type alias
CommonDep = Annotated[dict, Depends(common_parameters)]

@app.get("/products")
# defined parameters of route function main likhna Depends() main 
async def get_products(commons: CommonDep):
  return commons

@app.get("/posts")
# defined parameters of route function main likhna Depends() main 
async def get_posts(commons: CommonDep):
  return commons

# def current_user():
#     return {"name": "Talha"}

# @app.get("/profile")
# def profile(user = Depends(current_user)):
#     return user





  