import requests
import random
import time


SERVER_URL = "http://127.0.0.1:5000/api/sensor"

DEVICE_ID = "ESP32_001"


while True:

    temperature = round(
        random.uniform(20, 40), 2
    )

    humidity = round(
        random.uniform(40, 80), 2
    )

    air_quality = round(
        random.uniform(50, 200), 2
    )

    data = {
        "device_id": DEVICE_ID,
        "temperature": temperature,
        "humidity": humidity,
        "air_quality": air_quality
    }

    try:

        response = requests.post(
            SERVER_URL,
            json=data
        )

        print("Sensor Data:")
        print(data)

        print("Server Response:")
        print(response.json())

    except requests.exceptions.ConnectionError:

        print("Server is not running.")

    time.sleep(5)