import os
import time

class Config(object):
    # Get a bot token from botfather
    TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "7798706143:AAHsAm7SJEswWq4szQQSgK6D5Jb-aFkxDig")
    if not TELEGRAM_BOT_TOKEN:
        raise ValueError("Error: TELEGRAM_BOT_TOKEN is not set. Please check your environment variables.")

    # Get from my.telegram.org
    API_ID = os.environ.get("API_ID", "22884130")
    try:
        API_ID = int(API_ID) if API_ID else 0
    except ValueError:
        API_ID = 0
    if not API_ID:
        raise ValueError("Error: API_ID is not set or invalid. Please check your environment variables.")

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "a69e8b16dac958f1bd31eee360ec53fa")
    if not API_HASH:
        raise ValueError("Error: API_HASH is not set. Please check your environment variables.")

    # Database URL from MongoDB Atlas
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Fugui:tianlu@cluster0.6hyrp0r.mongodb.net/?appName=Cluster0")
    if not DATABASE_URI:
        raise ValueError("Error: DATABASE_URI is not set. Please check your environment variables.")

    # Your database name from MongoDB
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

    # ID of users that can use the bot commands
    AUTH_USERS = set()
    auth_users_str = os.environ.get("AUTH_USERS", "7840980054")
    if auth_users_str:
        AUTH_USERS = set(str(x).strip() for x in auth_users_str.split(","))
    else:
        print("Warning: AUTH_USERS is not set. Bot commands may not work properly.")

    # To save user details
    SAVE_USER = os.environ.get("SAVE_USER", "yes").lower() in ("yes", "true", "1", "y")

    # Heroku API key to check dyno status
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

    # Optional: Alternate bot commands
    ADD_FILTER_CMD = os.environ.get("ADD_FILTER_CMD", "add")
    DELETE_FILTER_CMD = os.environ.get("DELETE_FILTER_CMD", "del")
    DELETE_ALL_CMD = os.environ.get("DELETE_ALL_CMD", "delall")
    CONNECT_COMMAND = os.environ.get("CONNECT_COMMAND", "connect")
    DISCONNECT_COMMAND = os.environ.get("DISCONNECT_COMMAND", "disconnect")

    # Bot start time
    BOT_START_TIME = time.time()

    # Debugging: Print only non-sensitive info during startup
    print(f"Bot started at: {time.ctime(BOT_START_TIME)}")
    print(f"API_ID: {API_ID}")
    print(f"DATABASE_NAME: {DATABASE_NAME}")
    print(f"AUTH_USERS count: {len(AUTH_USERS)}")
    print(f"SAVE_USER: {SAVE_USER}")
    
    # DO NOT print sensitive credentials like tokens, API hashes, or database URIs
