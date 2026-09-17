import sqlite3

DATABASE = "data/iot.db"


def create_database():
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT NOT NULL,
            temperature REAL NOT NULL,
            humidity REAL NOT NULL,
            air_quality REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def insert_data(device_id, temperature, humidity, air_quality):
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO sensor_data
        (device_id, temperature, humidity, air_quality)
        VALUES (?, ?, ?, ?)
    """, (
        device_id,
        temperature,
        humidity,
        air_quality
    ))

    connection.commit()
    connection.close()


def get_latest_data():
    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM sensor_data
        ORDER BY id DESC
        LIMIT 20
    """)

    data = cursor.fetchall()

    connection.close()

    return [dict(row) for row in data]