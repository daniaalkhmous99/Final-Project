from flask import Flask, request, jsonify, send_from_directory
from database import get_recommendation
import os

app = Flask(__name__, static_folder='../frontend')

@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    user_input = data.get('input', '')
    result = get_recommendation(user_input)
    return jsonify({'recommendation': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)