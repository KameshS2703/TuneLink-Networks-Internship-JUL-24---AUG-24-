from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

JDoodle_ClientID = '2a31a1c18d363c02604a505c02d0b8cc'
JDoodle_ClientSecret = '34f31b5494c3c81aae6e6f82ceb301517d4deda3cc52d1d7a19e89d6b212f80f'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_code():
    data = request.get_json()
    language = data['language']
    code = data['code']
    filename = f'program.{language_extension(language)}'
    
    with open(filename, 'w') as f:
        f.write(code)
    
    return jsonify({'message': 'Code saved successfully!'})

@app.route('/run', methods=['POST'])
def run_code():
    data = request.get_json()
    language = data['language']
    code = data['code']

    language_mapping = {
        'c': 'c',
        'cpp': 'cpp',
        'java': 'java',
        'python': 'python3',
        'sql': 'sql'
    }

    payload = {
        'script': code,
        'language': language_mapping.get(language, 'python3'),
        'versionIndex': '0',
        'clientId': JDoodle_ClientID,
        'clientSecret': JDoodle_ClientSecret
    }

    response = requests.post('https://api.jdoodle.com/v1/execute', json=payload)
    result = response.json()

    return jsonify({'output': result.get('output', 'Error occurred during execution')})

def language_extension(language):
    return {
        'c': 'c',
        'cpp': 'cpp',
        'java': 'java',
        'python': 'py',
        'sql': 'sql'
    }.get(language, 'txt')

if __name__ == '__main__':
    app.run(debug=True)
