from typing import List
import re

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import nltk
nltk.download('punkt')

from config import config
from tag_generation.logger import logging

logger = logging.getLogger(__name__)

T5_TAGS_MODEL_PATH = config.T5_TAGS_MODEL_PATH
MAX_NEW_TOKENS = config.MAX_NEW_TOKENS
NUM_BEAMS = config.NUM_BEAMS

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

tokenizer = AutoTokenizer.from_pretrained(T5_TAGS_MODEL_PATH)
model = AutoModelForSeq2SeqLM.from_pretrained(T5_TAGS_MODEL_PATH)
model.to(device)

def generate_t5_tags(text: str) -> List[str]:
    logger.info('Started tags generation.')
    logger.info('Generating inputs.')
    inputs = tokenizer([text], max_length=512, truncation=True, return_tensors='pt')
    inputs.to(device)
    logger.info('Generating output.')
    output = model.generate(**inputs, num_beams=NUM_BEAMS, max_new_tokens=MAX_NEW_TOKENS)
    decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
    tags = list(set(decoded_output.strip().split(', ')))
    logger.info('Cleaning the tags.')
    cleaned_tags = []
    for tag in tags:
        tag = re.sub(r'[^a-zA-Z]', '', tag)
        if tag not in cleaned_tags:
            tag = tag.lower()
            cleaned_tags.append(tag)
    logger.info('Finished tags generation.')

    return cleaned_tags
