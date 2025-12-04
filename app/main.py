from fastapi import FastAPI, Depends, HTTPException, Header
from typing import Annotated
from app.routers import router as user
from app.routers import verify_token

# app = FastAPI()

# ================================== Creating and using environment variables ===============================
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# Method 1
# os.getenv("API_SECRET_KEY")

# Method 2

@app.get("/")
def read_env():
  return {
    "api_secret" : os.getenv("API_SECRET_KEY"),
    "debug_mode" : os.getenv("DEBUG"),
  }





#===================================  Dependencies with yield  ======================================================================

# class OwnerError(Exception):
#   pass


# def get_username():
#   try:
#     yield "taha"
#   except OwnerError as e:
#     raise HTTPException(status_code=400, detail=f"Owner error : {e}")

# @app.get("/items/{item_id}")
# def get_items(item_id: str, username: Annotated[str, Depends(get_username)]):
  
#     data = {
#       "product 1": {"description" : "this is a description of product one", "ower": "ali"},
#       "product 2": {"description" : "this is a description of product two", "owner": "taha"},
#     }
    
#     if item_id not in data:
#       raise HTTPException(status_code=404, detail="Item not found")
    
#     item = data[item_id]
    
#     if item['owner'] != username:
#       raise OwnerError(username)
#     return item
      
      
  
    







#===================================  Dependencies for a Group of Path Operation   ===================================================


# app.include_router(user)

# 2 Method using for dependency injection 
# app.include_router(user, dependencies=[Depends(verify_token)])




#===================================  Dependencies in Path Operation Decoratores  ===================================================

# async def verify_token(x_token : Annotated[str, Header()]):
#   if x_token != "secret123":
#     raise HTTPException(status_code=400, detail="X-Token header Invalid")
#   return x_token


# @app.get("/items", dependencies=[Depends(verify_token)])
# async def get_items():
#   return { "data" : "All Items"}





#=================================== Creating Dependencis Class ===================================================

# class CommonQueryParams:
#   def __init__(self, q: str | None = None, skip: int = 0, limit : int = 100):
    
#     self.q = q
#     self.skip = skip
#     self.limit = limit
    
# # Using Class Dependencies in Endpoints or routes


# comDep = Annotated[CommonQueryParams, Depends(CommonQueryParams)]

# @app.get("/items")
# async def get_items(common: comDep):
  
#   return common
  


    
    


# ===================================== Hierarchical Dependencies ========================================================

# A dependency khud kisi aur dependency par depend karti ho.
# Yani ek dependency ke andar bhi Depends() use hota hai.

# async def user_auth():
#   return  {"user_id": "123"}



# async def user_role(user: Annotated[dict, Depends(user_auth)]):
#   return {"user_id" : user["user_id"], "role": "admin"}


# @app.get("/admin")
# async def admin_only(role: Annotated[dict, Depends(user_role)]):
#   return role



# def decode_token(token: str):
#     if token != "secret123":
#         raise HTTPException(401, "Invalid token")
#     return {"user_id": 1}



# def get_current_user(data = Depends(decode_token)):
#     return {"id": data["user_id"], "name": "Talha"}
  


# @app.get("/profile")
# def profile(user = Depends(get_current_user)):
#     return {"profile": user}
  
  

  
  
#   /profile (route)
#     ↑
# get_current_user (dependency)
#     ↑
# decode_token (dependency)



  
  



# ============================= Sync and Async Dependency Injection =====================================================

# sync Dependency
# def sync_dep():
#   return { "message" : "I'm sync"}


# # async Dependency
# async def async_dep():
#   return { "message" : "I'm async"}


# @app.get("/test")
# async def get(asyncresult: Annotated[dict, Depends(async_dep)], syncresult: Annotated[dict, Depends(sync_dep)]):
#   return  {"sync": syncresult, "async" : asyncresult}
  




# ===================== Creating Dependency Injection =====================================

# Creating Dependency Function
# async def common_parameters(q:str | None =None , skip: int = 0, limit: int = 100):
#   return {"q": q, "skip": skip, "limit": limit}


# # Using Dependency in endpoints

# @app.get("/items")
# # defined parameters of route function main likhna Depends() main 
# async def get_items(commons: Annotated[dict, Depends(common_parameters)]):
#   return commons


# @app.get("/users")
# # defined parameters of route function main likhna Depends() main 
# async def get_users(commons: Annotated[dict, Depends(common_parameters)]):
#   return commons


# # Create a type alias
# CommonDep = Annotated[dict, Depends(common_parameters)]

# @app.get("/products")
# # defined parameters of route function main likhna Depends() main 
# async def get_products(commons: CommonDep):
#   return commons

# @app.get("/posts")
# # defined parameters of route function main likhna Depends() main 
# async def get_posts(commons: CommonDep):
#   return commons

# def current_user():
#     return {"name": "Talha"}

# @app.get("/profile")
# def profile(user = Depends(current_user)):
#     return user





  