from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_invoice(patient_name, sessions, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, f"Invoice for {patient_name}")
    y = 700
    total = 0
    for date, duration, fee in sessions:
        c.drawString(100, y, f"{date}: {duration} min - ${fee}")
        y -= 20
        total += fee
    c.drawString(100, y-20, f"Total Due: ${total}")
    c.save()
