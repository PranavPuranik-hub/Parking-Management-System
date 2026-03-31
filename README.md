# 🚀 AI-Powered Parking Management System + Blog Generator

A full-stack smart parking system built with **FastAPI**, **MongoDB**, and a modern **HTML/CSS/JS frontend**, now enhanced with an **AI-powered chatbot** that generates blog content for NGO/social activities.

---

## 🌟 Features

### 🅿️ Parking Management

* 🚗 Multi-vehicle support (Car, Bus, Truck, etc.)
* 🅿️ 25-slot live parking capacity tracking
* 💰 Real-time revenue calculation
* 📋 Activity logs (entry & exit history)
* 🔍 Search parked vehicles by number
* ⚠️ Duplicate vehicle detection
* 🗑 Reset all records

---

### 🤖 AI Blog Generator (NEW 🔥)

* 💬 Chatbot-based UI (like WhatsApp)
* 🧠 Generates blogs from user input
* ✍️ Creates NGO/event-based content automatically
* ⚡ One-click blog creation
* 🎯 Converts real-world activities into publish-ready content

---

## 🛠️ Tech Stack

| Layer      | Technology            |
| ---------- | --------------------- |
| Frontend   | HTML, CSS, JavaScript |
| Backend    | Python, FastAPI       |
| Database   | MongoDB               |
| AI         | OpenAI API            |
| Deployment | Render / Vercel       |

---

## 📁 Project Structure

```
project/
├── index.html          # Frontend dashboard
├── blog.html           # Blog page with AI chatbot
├── main.py             # FastAPI backend
├── requirements.txt
├── render.yaml
├── .env
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd project
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup Environment Variables

Create `.env` file:

```env
MONGO_URL=your_mongodb_connection
OPENAI_API_KEY=your_openai_key
```

---

### 4️⃣ Run Backend Server

```bash
uvicorn main:app --reload
```

Server runs on:
👉 http://localhost:8000

---

### 5️⃣ Open Frontend

Open in browser:

```bash
index.html
```

---

## 🔌 API Endpoints

### 🅿️ Parking APIs

| Method | Endpoint | Description      |
| ------ | -------- | ---------------- |
| GET    | `/data`  | Get parking data |
| POST   | `/park`  | Add vehicle      |
| POST   | `/exit`  | Remove vehicle   |
| POST   | `/reset` | Clear data       |

---

### 🤖 AI Blog API (NEW)

| Method | Endpoint         | Description            |
| ------ | ---------------- | ---------------------- |
| POST   | `/generate-blog` | Generate blog using AI |

---

## 🧠 How AI Chatbot Works

1. User opens chatbot 💬
2. Chatbot asks:

   * Event name
   * Date
   * Location
   * Details
3. Data is sent to backend
4. OpenAI generates blog
5. Blog is displayed as UI card

---

## 💡 Example AI Output

```
🌱 Tree Plantation Drive

On June 10, 2025, we organized a meaningful tree plantation drive...
```

---

## 🚀 Deployment

### Backend (Render)

* Use `render.yaml` config 
* Auto deploy from GitHub

---

### Frontend (Vercel)

* Upload static files
* Connect to backend API

---

## 📦 Requirements

From your project: 

```
fastapi
uvicorn[standard]
pymongo
python-dotenv
pydantic
```

---

## 🔒 Security Notes

* Do NOT expose API keys
* Restrict CORS in production
* Add authentication for admin features

---

## 🧠 Future Improvements

* 🎤 Voice-based chatbot
* 🌐 Multi-language support
* 🗄️ Blog database storage
* 📊 Admin dashboard
* 📸 Auto image generation

---

## 🎯 Project Highlight (For Interview / KT)

👉
**“We developed a full-stack parking management system and enhanced it with an AI-powered chatbot that converts user input into structured blog content using LLM APIs.”**

---

## 🙌 Author

Developed by **Rakshith K R**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
