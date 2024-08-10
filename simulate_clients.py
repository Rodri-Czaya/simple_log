import requests
import threading
import random
import time
from datetime import datetime, timezone

URL = "http://localhost:5555/log"

log_levels = ["INFO", "DEBUG", "ERROR"]
services = ["ServiceA", "ServiceB", "ServiceC"]

def generate_log():
    log = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "service_name": random.choice(services),
        "log_level": random.choice(log_levels),
        "message": "Este es un mensaje de log."
    }
    response = requests.post(URL, json=log)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Headers: {response.headers}")
    print(f"Response Text: {response.text}")  # Print the raw response text
    try:
        print(f"Response JSON: {response.json()}")  # Try to print the JSON response
    except ValueError:
        print("Response is not in JSON format")

def simulate_client(client_id):
    while True:
        generate_log()
        time.sleep(random.uniform(0.5, 2.0))

if __name__ == "__main__":
    clients = []
    for i in range(3):
        client_thread = threading.Thread(target=simulate_client, args=(i,))
        clients.append(client_thread)
        client_thread.start()

    for client in clients:
        client.join()
