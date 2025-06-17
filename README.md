WeasyPrint PDF Generator (Jinja2 + Flask)

A simple **PDF generator** using [WeasyPrint](https://weasyprint.org/) for the backend and plain HTML/CSS/JavaScript for the frontend. It supports **bulk and individual PDF generation** using data rendered with **Jinja2 templates**.

---

## 🚀 Features

* Generate PDFs (bulk or per record)
* Uses Jinja2 for templating
* REST API built with Flask
* HTML/CSS for clean PDF layout
* Frontend and backend are separated
* Hosted on Render (backend) and Vercel (frontend)

---

## 🧪 How It Works

1. Frontend fetches data from `/api/data`
2. UI shows a dynamic table
3. Buttons call:

   * `/pdf/bulk` → generate full PDF
   * `/pdf/individual/<id>` → generate one record
4. WeasyPrint renders the PDF from HTML + CSS

---

## 🛠 Local Setup

### 📦 Backend (Python Flask + WeasyPrint)

bash
git clone https://github.com/your_username/PDF_Generation.git
cd weasyprint_demo
pip install -r requirements.txt
python app.py

> Make sure you have WeasyPrint system dependencies installed.

### 💻 Frontend (HTML + JS)

* Open `index.html` using Live Server (VSCode) or run:
bash
cd weasyprint-ui
python -m http.server

---

## ☁️ Deployment

* **Backend**: Host on Render (use `gunicorn`, and install `flask-cors`)
* **Frontend**: Host static files on Vercel

---

## 📎 API Endpoints

| Endpoint               | Description             |
| ---------------------- | ----------------------- |
| `/api/data`            | Returns JSON data       |
| `/pdf/bulk`            | Generates full report   |
| `/pdf/individual/<id>` | Generates single record |

---

## 📚 Tech Stack

* Flask
* WeasyPrint
* Jinja2
* HTML, CSS, JavaScript

---

## 👨‍💻 Author

Developed by **Manuel Olarve**