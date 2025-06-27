from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/.well-known/discord')
def serve_discord():
    return send_from_directory('.well-known', 'discord')

@app.route('/')
def index():
    return 'Online'
