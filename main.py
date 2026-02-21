from fastapi import FastAPI
from src.routes import router as testRouter

app = FastAPI()
app.include_router(testRouter)

@app.get("/")
def hello(): 
    return {
        "message": "Hello From FastAPI Server!"
    }
    
@app.get("/howAreYou")
def isOk():
    return {
        "message": "Hello From Farooq!"
    }
    
items = [
    {"id":1, "item":"rice"},
    {"id":2, "item":"apple"},
]
    
@app.get("/items")
def getItems():
    return items

# Path Parameters
@app.get("/item/{itemId}")
def getItemById (itemId:int ):
    for item in items:
        if (item["id"] == itemId):
            return item
    return {
        "message": "Item Not Found!"
    }

# Query Parameters 
@app.get("/search")
def searchItem (itemName:str):
    for item in items:
        if (item["item"] == itemName):
            return item
    return {
        "message": "Item Not Found!"
    }

# Post Request
@app.post("/addItem")
def addItem (item:dict):
    items.append(item)
    return {
        "message": "Item Added Successfully!",
        "items": items
    }
