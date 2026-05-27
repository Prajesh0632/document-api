import firebase_admin
from firebase_admin import credentials, firestore
import json

from config import get_settings

db = None

def init_firebase():
    global db

    if db is not None:
        return db

    if firebase_admin._apps:
        db = firestore.client()
        return db

    settings = get_settings()

    if settings.is_production:
        # Production: Load from FIREBASE_KEY_JSON environment variable
        if not settings.firebase_key_json:
            raise ValueError("FIREBASE_KEY_JSON environment variable is required in production mode")
        try:
            firebase_key_dict = json.loads(settings.firebase_key_json)
            cred = credentials.Certificate(firebase_key_dict)
        except json.JSONDecodeError:
            raise ValueError("FIREBASE_KEY_JSON is not valid JSON")
    else:
        # Development: Load from file path
        cred = credentials.Certificate(settings.firebase_key_path)

    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db

def get_db():
    return db or init_firebase()
