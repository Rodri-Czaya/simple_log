from flask import Flask, request, jsonify
import psycopg2
from datetime import datetime, timezone
import os

app = Flask(__name__)

DB_HOST = "127.0.0.1"
DB_NAME = "logs"
DB_USER = "rodriczaya"
DB_PASSWORD = "penguin"

def get_db_connection():
    conexion = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=os.getenv("penguin")
    )
    return conexion

@app.route('/log', methods=['POST'])
def log_event():
    data = request.json
    timestamp = data.get('timestamp', datetime.now(timezone.utc).isoformat())
    service_name = data.get('service_name')
    log_level = data.get('log_level')
    message = data.get('message')
    
    conexion = get_db_connection()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO logs (timestamp, service_name, log_level, message) VALUES (%s, %s, %s, %s)",
        (timestamp, service_name, log_level, message)
    )
    conexion.commit()
    cursor.close()
    conexion.close()

    response = jsonify({"status": "success"})
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
