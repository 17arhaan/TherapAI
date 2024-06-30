import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://root:Ck243414$@localhost/mental_health_chatbot'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
