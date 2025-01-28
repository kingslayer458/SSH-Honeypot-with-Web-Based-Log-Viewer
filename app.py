from flask import Flask, render_template
import threading
import time

app = Flask(__name__)

# Shared data structure to store logs
logs = []

def read_logs():
    global logs
    while True:
        try:
            with open('ssh_honeypot.log', 'r') as f:
                logs = f.readlines()
        except FileNotFoundError:
            logs = ["Log file not found."]
        except Exception as e:
            logs = [f"Error reading log file: {e}"]
        time.sleep(1)

@app.route('/')
def index():
    print("Logs:", logs)  # Debug statement
    return render_template('index.html', logs=logs)

if __name__ == "__main__":
    # Start a thread to read logs
    threading.Thread(target=read_logs, daemon=True).start()
    app.run(host='0.0.0.0', port=5000, debug=True)