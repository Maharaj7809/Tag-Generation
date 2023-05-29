from flask import Flask, request, jsonify
from flask_cors import CORS

from tag_generation.logger import logging
from tag_generation.models_interface.t5_tags import generate_t5_tags
from tag_generation.models_interface.text_2_tags import generate_text_2_tag_text
from config import config

logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app=app)

def get_formated_response(
    status,
    message,
    tags
) -> dict:
    
    return jsonify(
        {
            'status': status,
            'message': message,
            'tags': tags
        }
    )

@app.route('/')
def home():
    return 'v0.0.1'

@app.route('/api/generate/tags', methods=['POST'])
def api_image():
    logger.info('A new request came /api/image')
    if request.is_json:
        body = request.get_json()
        logger.info(body)
        if 'text' in body.keys():
            try:
                one_tags = generate_t5_tags(body['text'])
                two_tags = generate_text_2_tag_text(body['text'])
                tags = list(set(one_tags + two_tags))
                return get_formated_response(
                    1,
                    'Success',
                    tags
                )
            except:
                logger.info('Error performing the operation.')
                return get_formated_response(
                    -1,
                    'Failure',
                    []
                )

        else:
            logger.info('Request has no parameter text.')
            return get_formated_response(
                -1,
                'Request has no parameter text.',
                []
            )
    else:
        logger.info('Request has no body.')
        return get_formated_response(
            -1,
            'Request has no body.',
            []
        )
