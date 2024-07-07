from os import environ as env

class Telegram:
    API_ID = int(env.get("TG_API_ID", 16768772))
    API_HASH = env.get("TG_API_HASH", "08d78fb05bdb90f1be4a4f1f0fef5f1e")
    BOT_TOKEN = env.get("TG_BOT_TOKEN", "abc")
    BOT_USERNAME = env.get("TG_BOT_USERNAME", "DrReactBot")
    DELAY = int(env.get("DELAY"))
    EMOJIS = [
        "👍", "🔥", 
        "👏",
        "🤩",
        "👌",
        "😍",
        "💋",
        "👀",
        "😇",
        "🗿",

    ]

LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'pyrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
