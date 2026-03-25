# 🅿️ The Great Parking Management System

A full-stack parking lot management dashboard built with a **FastAPI** backend, **MySQL** database, and a modern **HTML/CSS/JS** frontend. Manage vehicle entries, exits, revenue tracking, and activity logs — all in real time.

---

## 📸 Features

- 🚗 **Multi-vehicle support** — Car, Auto Rickshaw, Bus, Truck, Motorcycle, Van
- 🅿️ **25-slot capacity management** with live visual indicators
- 💰 **Revenue tracking** — auto-calculated from entry fees
- 📋 **Activity log** — last 30 entries and exits
- 🔍 **Search & exit** — find parked vehicles by plate number
- ⚠️ **Duplicate plate detection** — prevents double-parking
- 🗑️ **Reset** — clear all records with one click
- 📱 **Responsive UI** — works on desktop and mobile

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, Vanilla JavaScript |
| Backend | Python, FastAPI |
| Database | MySQL |
| DB Driver | `mysql-connector-python` |
| Config | `python-dotenv` |

---

## 📁 Project Structure

```
parking-management/
├── index.html          # Frontend dashboard
├── main.py             # FastAPI backend
├── .env                # Environment variables (not committed)
├── .env.example        # Sample env file
├── requirements.txt    # Python dependencies
└── README.md
```

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.8+
- MySQL 8.0+
- A modern web browser

---

### 1. Clone the Repository

```bash
git clone https://github.com/PranavPuranik-hub/parking-management-system.git
cd parking-management-system
```

### 2. Set Up the Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```env
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=parking_db
```

### 4. Set Up the MySQL Database

Log into MySQL and run:

```sql
CREATE DATABASE parking_db;
USE parking_db;

CREATE TABLE vehicles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    fee INT NOT NULL,
    icon VARCHAR(10) NOT NULL,
    plate VARCHAR(30) NOT NULL UNIQUE,
    time VARCHAR(30) NOT NULL
);

CREATE TABLE logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    icon VARCHAR(10) NOT NULL,
    plate VARCHAR(30) NOT NULL,
    fee INT NOT NULL,
    time VARCHAR(30) NOT NULL,
    type ENUM('in', 'out') NOT NULL
);
```

### 5. Start the Backend Server

```bash
uvicorn main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`.

### 6. Open the Frontend

Simply open `index.html` in your browser. No build step required.

> **Note:** Make sure the backend is running before using the dashboard, as all data is fetched from the API.

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/data` | Fetch all parked vehicles, logs, count, and revenue |
| `POST` | `/park` | Park a new vehicle |
| `POST` | `/exit` | Remove a vehicle (exit) |
| `POST` | `/reset` | Clear all records |

### Request / Response Examples

**POST `/park`**
```json
// Request
{
  "name": "Car",
  "fee": 100,
  "icon": "🚗",
  "plate": "KA 01 AB 1234"
}

// Response
{
  "message": "Vehicle parked",
  "id": 7
}
```

**POST `/exit`**
```json
// Request
{ "id": 7 }

// Response
{ "message": "Vehicle exited" }
```

---

## 💸 Parking Fee Structure

| Vehicle | Fee |
|---------|-----|
| 🏍️ Motorcycle | ₹50 |
| 🛺 Auto Rickshaw | ₹75 |
| 🚗 Car | ₹100 |
| 🚐 Van | ₹150 |
| 🚌 Bus | ₹200 |
| 🚛 Truck | ₹250 |

---

## 📦 Requirements

```txt
fastapi
uvicorn
mysql-connector-python
python-dotenv
pydantic
```

Install all at once:

```bash
pip install -r requirements.txt
```

---

## 🔒 Security Notes

- Never commit your `.env` file. Add it to `.gitignore`.
- CORS is currently set to `allow_origins=["*"]` for development. Restrict this in production.
- Consider adding authentication before deploying publicly.

---

## 🚀 Deployment Tips

- Use **Gunicorn** with Uvicorn workers for production:
  ```bash
  gunicorn main:app -k uvicorn.workers.UvicornWorker -w 4
  ```
- Serve the frontend via **Nginx** or any static file host.
- Use a managed MySQL instance (e.g., AWS RDS, PlanetScale) in production.

---


## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

    finally:
        cursor.close()
        db.close()
        
