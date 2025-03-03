from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("message")
def handle_message(msg):
    print("📩 Received:", msg)
    socketio.send("✅ Server response: " + str(msg))

@app.route("/")
def index():
    return "🚀 WebSocket Server is running!"

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)