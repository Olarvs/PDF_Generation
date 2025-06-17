from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from datetime import datetime
import os
from data import sample_data

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("report_template.html")

os.makedirs("output/", exist_ok=True)
os.makedirs("output/individual", exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_date = datetime.now().strftime("%B %d, %Y")


# Full report with bulk records
full_html = template.render(people=sample_data, date=report_date)
full_report_path = f"output/full_report_{timestamp}.pdf"
HTML(string=full_html).write_pdf(full_report_path)
print(f"✅ Full report created: {full_report_path}")

# Individual report
for i, person in enumerate(sample_data, start=1):
    html_content = template.render(people=[person], date=report_date)
    individual_path = f"output/individual/record_{i}_{timestamp}.pdf"
    HTML(string=html_content).write_pdf(individual_path)
    print(f"✅ Individual report created: {individual_path}")
