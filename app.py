from flask import Flask, render_template, request, jsonify
from commiter_ai import generate_commit_message

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    repo_path = request.form.get('repo_path')
    branch = request.form.get('branch') or 'main'
    
    try:
        commit_message = generate_commit_message(repo_path, branch).text
        return jsonify({'message': commit_message, 'status': 'success'})
    except Exception as e:
        return jsonify({'message': str(e), 'status': 'error'})

if __name__ == '__main__':
    app.run(debug=True)