
import sqlite3
from pathlib import Path

DATABASE = Path(__file__).parent / "ticketing.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():

    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            venue TEXT NOT NULL,
            event_date TEXT NOT NULL,
            price_sats INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INTEGER NOT NULL,
            customer_name TEXT NOT NULL,
            customer_email TEXT NOT NULL,
            payment_hash TEXT UNIQUE,
            payment_request TEXT,
            ticket_code TEXT UNIQUE,
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (event_id) REFERENCES events(id)
        )
    """)

    connection.commit()
    connection.close()

    print("Database initialized successfully!")


# Save a new event
def create_event(title, description, venue, event_date, price_sats, quantity):

    connection = get_db_connection()

    connection.execute("""
        INSERT INTO events (
            title, description, venue, event_date, price_sats, quantity
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (title, description, venue, event_date, price_sats, quantity))

    connection.commit()
    connection.close()


# Retrieve all events
def get_all_events():

    connection = get_db_connection()

    events = connection.execute("""
        SELECT * FROM events ORDER BY event_date ASC
    """).fetchall()

    connection.close()

    return events


# Retrieve one event using its ID
def get_event_by_id(event_id):

    connection = get_db_connection()

    event = connection.execute("""
        SELECT * FROM events WHERE id = ?
    """, (event_id,)).fetchone()

    connection.close()

    return event

def seed_events():
    
    connection = get_db_connection()

    # Check whether events already exist
    count = connection.execute(
        "SELECT COUNT(*) FROM events"
    ).fetchone()[0]

    # Only add sample events if the database is empty
    if count == 0:

        sample_events = [
            (
                "Malawi Tech Summit",
                "A gathering of developers, entrepreneurs and technology enthusiasts.",
                "Lilongwe, Malawi",
                "2026-12-15",
                10000,
                100
            ),
            (
                "Entrepreneurs Meetup",
                "Connect with business owners, startup founders and aspiring entrepreneurs.",
                "Blantyre, Malawi",
                "2026-12-20",
                5000,
                100
            ),
            (
                "Digital Skills Workshop",
                "A practical workshop to develop digital and technology skills.",
                "Mzuzu, Malawi",
                "2027-01-10",
                3000,
                100
            )
        ]

        connection.executemany("""
            INSERT INTO events (
                title,
                description,
                venue,
                event_date,
                price_sats,
                quantity
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, sample_events)

        connection.commit()

        print("Sample events added successfully!")

    else:
        print("Events already exist. No sample events added.")

    connection.close()