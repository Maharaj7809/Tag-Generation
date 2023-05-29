import os

from dotenv import load_dotenv
load_dotenv()

MAX_NEW_TOKENS = int(os.getenv('MAX_NEW_TOKENS'))
NUM_BEAMS = int(os.getenv('NUM_BEAMS'))
T5_TAGS_MODEL_PATH = os.getenv('T5_TAGS_MODEL_PATH')
TEXT_TO_TAGS_MODEL_PATH = os.getenv('TEXT_TO_TAGS_MODEL_PATH')

cwd = os.getcwd()

LOG_DIR = 'app_log'
os.makedirs(
    os.path.join(
        cwd,
        LOG_DIR
    ),
    exist_ok=True
)
