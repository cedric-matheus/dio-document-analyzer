import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    CONTAINER_NAME = os.getenv('CONTAINER_NAME')
    CONNECTION_STRING = os.getenv('CONNECTION_STRING')
    STORAGE_NAME = os.getenv('STORAGE_NAME')
    DOC_ANALYZER_KEY = os.getenv('DOC_ANALYZER_KEY')
    DOC_ANALYZER_URL = os.getenv('CONTAINER_NAME')