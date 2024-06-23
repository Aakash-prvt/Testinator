from bot import TelegramBot, logger
from flask import Flask
import os
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Render!'

def run_flask():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

def run_telegram_bot():
    logger.info('Initializing...')
    TelegramBot.run()

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    bot_thread = threading.Thread(target=run_telegram_bot)

    flask_thread.start()
    bot_thread.start()

    flask_thread.join()
    bot_thread.join()
