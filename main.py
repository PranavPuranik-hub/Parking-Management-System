from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import mysql.connector
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
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
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT", 3306))
    )

class Vehicle(BaseModel):
    name: str
    fee: int
    icon: str
    plate: str

class ExitVehicle(BaseModel):
    id: int

# Serve the frontend
@app.get("/")
def serve_frontend():
    return FileResponse("index.html")

@app.post("/park")
def park_vehicle(v: Vehicle):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM vehicles WHERE plate=%s", (v.plate,))
        if cursor.fetchone():
            return {"error": "Vehicle already parked"}
        time = datetime.now().strftime("%d-%m-%Y %I:%M %p")
        cursor.execute(
            "INSERT INTO vehicles (name, fee, icon, plate, time) VALUES (%s,%s,%s,%s,%s)",
            (v.name, v.fee, v.icon, v.plate, time)
        )
        vehicle_id = cursor.lastrowid
        cursor.execute(
            "INSERT INTO logs (name, icon, plate, fee, time, type) VALUES (%s,%s,%s,%s,%s,%s)",
            (v.name, v.icon, v.plate, v.fee, time, "in")
        )
        db.commit()
        return {"message": "Vehicle parked", "id": vehicle_id}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        db.close()

@app.post("/exit")
def exit_vehicle(v: ExitVehicle):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM vehicles WHERE id=%s", (v.id,))
        vehicle = cursor.fetchone()
        if not vehicle:
            return {"error": "Vehicle not found"}
        time = datetime.now().strftime("%d-%m-%Y %I:%M %p")
        cursor.execute(
            "INSERT INTO logs (name, icon, plate, fee, time, type) VALUES (%s,%s,%s,%s,%s,%s)",
            (vehicle["name"], vehicle["icon"], vehicle["plate"], 0, time, "out")
        )
        cursor.execute("DELETE FROM vehicles WHERE id=%s", (v.id,))
        db.commit()
        return {"message": "Vehicle exited"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        db.close()

@app.get("/data")
def get_data():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM vehicles ORDER BY id DESC")
        vehicles = cursor.fetchall()
        cursor.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 30")
        logs = cursor.fetchall()
        count = len(vehicles)
        cursor.execute("SELECT SUM(fee) AS total FROM logs WHERE type='in'")
        result = cursor.fetchone()
        amount = result["total"] if result["total"] else 0
        return {"count": count, "amount": amount, "parked": vehicles, "log": logs}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        db.close()

@app.post("/reset")
def reset():
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM vehicles")
        cursor.execute("DELETE FROM logs")
        db.commit()
        return {"message": "All data cleared"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        db.close()
