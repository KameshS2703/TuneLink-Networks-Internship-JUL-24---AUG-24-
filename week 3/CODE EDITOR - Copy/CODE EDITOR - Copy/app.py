from flask import Flask, render_template, request, jsonify
import subprocess
import os

app = Flask(__name__)

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
    filename = f'program.{language_extension(language)}'
    
    with open(filename, 'w') as f:
        f.write(code)
    
    output = ''
    try:
        if language == 'c':
            executable = filename.split('.')[0]
            compile_command = f"gcc {filename} -o {executable}"
            compile_process = subprocess.run(compile_command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            if compile_process.returncode != 0:
                return jsonify({'output': compile_process.stderr.decode()})
            
            run_process = subprocess.run(f'./{executable}', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = run_process.stdout.decode() + run_process.stderr.decode()
        elif language == 'cpp':
            executable = filename.split('.')[0]
            compile_command = f"g++ {filename} -o {executable}"
            compile_process = subprocess.run(compile_command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            if compile_process.returncode != 0:
                return jsonify({'output': compile_process.stderr.decode()})
            
            run_process = subprocess.run(f'./{executable}', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = run_process.stdout.decode() + run_process.stderr.decode()
        elif language == 'java':
            compile_process = subprocess.run(f"javac {filename}".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            if compile_process.returncode != 0:
                return jsonify({'output': compile_process.stderr.decode()})
            
            run_process = subprocess.run(f"java {filename.split('.')[0]}".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = run_process.stdout.decode() + run_process.stderr.decode()
        elif language == 'python':
            run_process = subprocess.run(f"python {filename}".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = run_process.stdout.decode() + run_process.stderr.decode()
        elif language == 'sql':
            output = 'SQL execution not supported in this example'
        else:
            output = 'Unsupported language'
    finally:
        if os.path.exists(filename):
            os.remove(filename)
        if language in ['c', 'cpp', 'java'] and os.path.exists(filename.split('.')[0]):
            os.remove(filename.split('.')[0])
    
    return jsonify({'output': output})

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
