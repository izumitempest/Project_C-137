# Route handlers go here
from flask import Blueprint, request, jsonify
from .utils import extract_text_from_image, find_valid_reg_numbers

bp = Blueprint('main', __name__)

@bp.route('/scan', methods=['POST'])
def scan_id_card():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image_file = request.files['image']
    image_bytes = image_file.read()

    text = extract_text_from_image(image_bytes)
    reg_numbers = find_valid_reg_numbers(text)

    if not reg_numbers:
        return jsonify({"error": "No valid reg number found"}), 404

    return jsonify({
        "reg_numbers": reg_numbers,
        "raw_text": text
    })
