import json
import random
import time
from datetime import datetime

LEVELS = ["INFO", "WARN", "ERROR", "CRITICAL"]
MESSAGES = [
    "User login successful",
    "User failed authentication",
    "Database connection failed",
    "File not found",
    "Service started successfully",
    "Disk space running low",
    "API request timed out"
]

def generate_log():
    log = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "level": random.choice(LEVELS),
        "message": random.choice(MESSAGES)
    }
    return json.dumps(log)

if __name__ == "__main__":
    while True:
        print(generate_log(), flush=True)  # stdout output
        time.sleep(random.randint(1, 3))
