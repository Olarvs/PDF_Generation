from flask import Flask, render_template, send_file, abort, jsonify
from flask_cors import CORS
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from datetime import datetime
import os
import io
from data import sample_data

app = Flask(__name__)
CORS(app)
env = Environment(loader=FileSystemLoader("templates"))

os.makedirs("output/", exist_ok=True)
os.makedirs("output/individual", exist_ok=True)

@app.route("/api/data")
def get_data():
    return jsonify(sample_data)

@app.route("/table")
def table_page():
    return render_template("index.html")

@app.route("/")
def index():
    return "WeasyPrint PDF Generator API is running!"

@app.route("/pdf/bulk")
def generate_bulk_report():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_date = datetime.now().strftime("%B %d, %Y")
    template = env.get_template("report_template.html")

    full_html = template.render(people=sample_data, date=report_date)
    pdf_file = HTML(string=full_html).write_pdf()

    return send_file(
        io.BytesIO(pdf_file),
        download_name=f"full_report_{timestamp}.pdf",
        mimetype="application/pdf"
    )

@app.route("/pdf/individual/<int:id>")
def generate_individual_report(id):
    if id < 1 or id > len(sample_data):
        return abort(404, description="Invalid ID")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_date = datetime.now().strftime("%B %d, %Y")
    template = env.get_template("report_template.html")
    
    person = sample_data[id - 1]
    html_content = template.render(people=[person], date=report_date)
    pdf_file = HTML(string=html_content).write_pdf()

    return send_file(
        io.BytesIO(pdf_file),
        download_name=f"record_{id}_{timestamp}.pdf",
        mimetype="application/pdf"
    )

if __name__ == "__main__":
    app.run(debug=True)
