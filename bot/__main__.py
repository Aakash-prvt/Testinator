# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, I'm alive!"

def run_flask():
    # Get the port from the environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    logger.info('Initializing...')

    # Start the Flask app in a separate thread
    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    # Run the Telegram bot
    TelegramBot.run()
