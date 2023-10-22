# main.py

from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import random
import string

import fusion as fs 

app = FastAPI()

origins = [
    "https://chat.openai.com",
    "http://localhost",
    "http://localhost:5003",
    "http://localhost:9090",
    "http://0.0.0.0:9090",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return FileResponse(filename)

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    filename = '.well-known/ai-plugin.json'
    return FileResponse(filename)

@app.get("/openapi.yaml")
async def openapi_spec():
    filename = "openapi.yaml"
    return FileResponse(filename)

@app.get("/recommend/")
async def recommend(location: str, service: str, number: int):
    # Splitting the location string based on ':'
    locations = location.split(":")
    if len(locations) != 2:
        raise HTTPException(status_code=400, detail="Invalid location format. Expected format: 'string1:string2'")

    # Validate number
    if number <= 0:
        raise HTTPException(status_code=400, detail="Number should be a positive integer")

    print("recommend: location[%s:%s] service[%s] number[%d]" % (locations[0].strip(), locations[1].strip(), service, number))
    location = locations[0].strip()+","+locations[1].strip()

    return fs.search(fs.API_KEY, service, location)
                     

if __name__ == "__main__":
    import uvicorn
    from env import *

    setup_env(".env")
    fs.API_KEY=os.environ.get("ENV_YELP_FUSION_APIKEY")
    print("KEY=[%s]" % fs.API_KEY)
     
    uvicorn.run(app, host="0.0.0.0", port=9090)

