from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from pymongo import MongoClient
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from bson import ObjectId
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    client = MongoClient(os.getenv("MONGO_URL"))
    db = client.get_default_database()
    return client, db

class Vehicle(BaseModel):
    name: str
    fee: int
    icon: str
    plate: str

class ExitVehicle(BaseModel):
    id: str 

def serialize(doc):
    """Convert MongoDB document to JSON-serializable dict."""
    if doc is None:
        return None
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc

# Serve the frontend
@app.get("/")
def serve_frontend():
    return FileResponse("index.html")

@app.post("/park")
def park_vehicle(v: Vehicle):
    client, db = None, None
    try:
        client, db = get_db()
        vehicles = db["vehicles"]
        logs = db["logs"]

        # Check if vehicle already parked
        if vehicles.find_one({"plate": v.plate}):
            return JSONResponse(status_code=400, content={"error": "Vehicle already parked"})

        time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

        # Insert vehicle
        result = vehicles.insert_one({
            "name": v.name,
            "fee": v.fee,
            "icon": v.icon,
            "plate": v.plate,
            "time": time
        })

        # Insert log
        logs.insert_one({
            "name": v.name,
            "icon": v.icon,
            "plate": v.plate,
            "fee": v.fee,
            "time": time,
            "type": "in"
        })

        return {"message": "Vehicle parked", "id": str(result.inserted_id)}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    finally:
        if client: client.close()

@app.post("/exit")
def exit_vehicle(v: ExitVehicle):
    client, db = None, None
    try:
        client, db = get_db()
        vehicles = db["vehicles"]
        logs = db["logs"]

        vehicle = vehicles.find_one({"_id": ObjectId(v.id)})
        if not vehicle:
            return JSONResponse(status_code=404, content={"error": "Vehicle not found"})

        time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

        # Insert exit log
        logs.insert_one({
            "name": vehicle["name"],
            "icon": vehicle["icon"],
            "plate": vehicle["plate"],
            "fee": 0,
            "time": time,
            "type": "out"
        })

        # Remove vehicle
        vehicles.delete_one({"_id": ObjectId(v.id)})

        return {"message": "Vehicle exited"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    finally:
        if client: client.close()

@app.get("/data")
def get_data():
    client, db = None, None
    try:
        client, db = get_db()
        vehicles = db["vehicles"]
        logs = db["logs"]

        parked = [serialize(v) for v in vehicles.find().sort("_id", -1)]
        log_list = [serialize(l) for l in logs.find().sort("_id", -1).limit(30)]

        count = len(parked)

        total_result = logs.aggregate([
            {"$match": {"type": "in"}},
            {"$group": {"_id": None, "total": {"$sum": "$fee"}}}
        ])
        total_list = list(total_result)
        amount = total_list[0]["total"] if total_list else 0

        return {"count": count, "amount": amount, "parked": parked, "log": log_list}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    finally:
        if client: client.close()

@app.post("/reset")
def reset():
    client, db = None, None
    try:
        client, db = get_db()
        db["vehicles"].delete_many({})
        db["logs"].delete_many({})
        return {"message": "All data cleared"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    finally:
        if client: client.close()
