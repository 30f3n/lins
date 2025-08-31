from flask import Flask, request, jsonify
from license_manager import generate_license, check_license

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    username = request.json.get('username')
    license_key = generate_license(username)
    return jsonify({'license_key': license_key})

@app.route('/verify', methods=['POST'])
def verify():
    license_key = request.json.get('license_key')
    if check_license(license_key):
        return jsonify({'status': 'valid'})
    else:
        return jsonify({'status': 'invalid'}), 403

if __name__ == '__main__':
    app.run(debug=True)
