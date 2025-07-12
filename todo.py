from fastapi import FastAPI, Query, Body
from fastapi.responses import JSONResponse
from models.todo import Todo as TodoModel
import uuid
import logging

logging.basicConfig(level=logging.INFO)


server = FastAPI()

todo_collection = [
    {
        "id":"1",
        "title":"Go to Gym",
        "action":"Everyevening 7 - 8 go to GYM"
    }
]

@server.get("/")
def root_handler():
    return {"message":"Welcome to Todo application"}

@server.get("/todo")
async def get_todos(count:int = None):
    if(count):
        return  todo_collection[:count]
    else:
        return todo_collection

@server.get("/todo/{id}")
def get_todo(id:str):
    return {item["id"]: item for item in todo_collection}

@server.post("/todo")
def create_todo(request_body:dict):
    request_body['id'] = str(uuid.uuid4())
    todo_collection.append(request_body)
    return JSONResponse(status_code=200,content={"message":"created"})

@server.put("/todo/{id}")
def update_todo(id: str, request_body:dict):
    try:
        for index,item in enumerate(todo_collection):
            if item['id'] == id:
                todo_collection[index] = request_body
                return JSONResponse(content={"message":"updated"}, status_code=204)
        else:
            return JSONResponse(status_code=404,content={"message":"Not found"})
    except Exception as e:
            return JSONResponse({"message":"invalid input"},status_code=400)
        
@server.delete("/todo/{id}")
async def delete_todo(id:str):
    try:
        logging.info(id)
        for index,item in enumerate(todo_collection):
            logging.info(item)
            if item['id'] == id:
                todo_collection.pop(index)
                return JSONResponse(status_code=200,content={"message":"Deleted"})
        else:
            return JSONResponse(status_code=404,content={"message":"Not found"})
    except Exception as e:
        logging.info(e)
            
