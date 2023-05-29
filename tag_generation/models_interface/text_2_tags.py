from typing import List
import re

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

from config import config
from tag_generation.logger import logging

logger = logging.getLogger(__name__)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

TEXT_TO_TAGS_MODEL_PATH = config.TEXT_TO_TAGS_MODEL_PATH
MAX_NEW_TOKENS = config.MAX_NEW_TOKENS
NUM_BEAMS = config.NUM_BEAMS

model = AutoModelForSeq2SeqLM.from_pretrained(TEXT_TO_TAGS_MODEL_PATH)
tokenizer = AutoTokenizer.from_pretrained(TEXT_TO_TAGS_MODEL_PATH)

model.to(device)

def generate_text_2_tag_text(text: str) -> List[str]:
    logger.info('Started tags generation.')
    logger.info('Generating inputs.')
    text = text.strip().replace('\n', '')
    text = f'Summarize: {text}'
    inputs = tokenizer([text], max_length=512,
                       truncation=True, return_tensors='pt')
    inputs.to(device)
    logger.info('Generating output.')
    tags_ids = model.generate(**inputs,
                              num_beams=4,
                              no_repeat_ngram_size=2,
                              max_length=20,
                              early_stopping=True)
    output = tokenizer.decode(tags_ids[0], skip_special_tokens=True)
    tags = output.split(', ')
    logger.info('Cleaning the tags.')
    cleaned_tags = []
    for tag in tags:
        tag = re.sub(r'[^a-zA-Z]', '', tag)
        if tag not in cleaned_tags:
            tag = tag.lower()
            cleaned_tags.append(tag)
    logger.info('Finished tags generation.')
    return cleaned_tags
