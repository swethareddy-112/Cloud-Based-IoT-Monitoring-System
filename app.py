from flask import Flask, render_template, request, jsonify
from database import create_database, insert_data, get_latest_data

app = Flask(__name__)

create_database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/sensor", methods=["POST"])
def receive_sensor_data():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No data received"
        }), 400

    device_id = data.get("device_id")
    temperature = data.get("temperature")
    humidity = data.get("humidity")
    air_quality = data.get("air_quality")

    if None in [device_id, temperature, humidity, air_quality]:
        return jsonify({
            "error": "Missing sensor data"
        }), 400

    insert_data(
        device_id,
        temperature,
        humidity,
        air_quality
    )

    return jsonify({
        "message": "Sensor data stored successfully"
    })


@app.route("/api/data", methods=["GET"])
def get_sensor_data():

    data = get_latest_data()

    return jsonify(data)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )