
from flask import Flask, render_template

from database import (
    init_db,
    seed_events,
    get_all_events,
    get_event_by_id
)

app = Flask(__name__)


# Homepage
@app.route("/")
def home():
    return render_template("index.html")


# Events page
@app.route("/events")
def events():
    all_events = get_all_events()
    return render_template("events.html", events=all_events)


# Event details page
@app.route("/events/<int:event_id>")
def event_details(event_id):
    event = get_event_by_id(event_id)

    if event is None:
        return "Event not found", 404

    return render_template("event_details.html", event=event)


# Checkout page
@app.route("/checkout")
def checkout():
    return render_template("checkout.html")


# Payment page
@app.route("/payment")
def payment():
    return render_template("payment.html")


# Digital ticket page
@app.route("/ticket")
def ticket():
    return render_template("ticket.html")


# Organiser dashboard
@app.route("/admin")
def admin():
    return render_template("admin.html")


# Create event page
@app.route("/create-event")
def create_event():
    return render_template("create_event.html")


# Verify ticket page
@app.route("/verify-ticket")
def verify_ticket():
    return render_template("verify_ticket.html")


# QR code testing page
@app.route("/test-qr")
def test_qr():
    return render_template("test_qr.html")


# Start the application
if __name__ == "__main__":
    init_db()
    seed_events()
    app.run(debug=True)
