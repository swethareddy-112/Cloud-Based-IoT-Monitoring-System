async function loadSensorData() {

    try {

        const response = await fetch("/api/data");

        const data = await response.json();

        if (data.length === 0) {
            return;
        }

        const latest = data[0];

        document.getElementById("temperature").innerText =
            latest.temperature + " °C";

        document.getElementById("humidity").innerText =
            latest.humidity + " %";

        document.getElementById("air_quality").innerText =
            latest.air_quality;

        document.getElementById("device").innerText =
            latest.device_id;


        const table =
            document.getElementById("sensorTable");

        table.innerHTML = "";

        data.forEach(item => {

            const row = `
                <tr>
                    <td>${item.device_id}</td>
                    <td>${item.temperature} °C</td>
                    <td>${item.humidity} %</td>
                    <td>${item.air_quality}</td>
                    <td>${item.timestamp}</td>
                </tr>
            `;

            table.innerHTML += row;

        });

    } catch (error) {

        console.log("Error:", error);

    }
}


loadSensorData();


// Refresh every 5 seconds
setInterval(loadSensorData, 5000);