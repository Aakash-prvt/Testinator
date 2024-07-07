from bot import TelegramBot, logger
import os
import threading
from flask import Flask
from pyrogram import Client

# Initialize Flask app for health check
health_app = Flask(__name__)

@health_app.route('/')
def health_check():
    return "Healthy", 200

def start_health_check_server():
    port = int(os.environ.get("PORT", 5000))
    health_app.run(host='0.0.0.0', port=port)


if __name__ == "__main__":
    # Start health check server in a separate thread
    threading.Thread(target=start_health_check_server).start()
    
    # Run the bot
    TelegramBot.run()

