import logging
from datetime import datetime
import os
import sys

from config import config

LOG_DIR = config.LOG_DIR

TIMESTAMP = f'{datetime.now().strftime("%Y-%m-%d_%H-%M")}'

FILE_NAME = f'logs_{TIMESTAMP}.log'

FILE_PATH = os.path.join(LOG_DIR, FILE_NAME)

logging.basicConfig(
    format='[%(asctime)s] - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler(FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)
