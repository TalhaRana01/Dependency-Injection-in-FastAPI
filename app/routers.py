from fastapi import APIRouter, HTTPException, Header, Depends
from typing import Annotated


# Create Dependency
async def verify_token(x_token : Annotated[str, Header()]):
  if x_token != "secret123":
    raise HTTPException(status_code=400, detail="X-Token header Invalid")
  return x_token


# 1 Method using for dependency injection 
# router = APIRouter(dependencies=[Depends(verify_token)])
router = APIRouter()


@router.get("/users")
async def get_users():
  return {"data" : "All Users"}
# @router.get("/users")
# async def get_users():
#   return {"data" : "All Users"}




