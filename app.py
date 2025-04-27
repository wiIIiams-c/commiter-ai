from flask import Flask, render_template, request, jsonify
from commiter_ai import generate_commit_message
from commit_summary import generate_commit_summary

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/commit_generator')
def commit_generator():
    return render_template('commit_generator.html')

@app.route('/commit_summary')
def commit_summary():
    return render_template('commit_summary.html')

@app.route('/generate', methods=['POST'])
def generate():
    repo_path = request.form.get('repo_path')
    branch = request.form.get('branch') or 'main'
    
    try:
        commit_message = generate_commit_message(repo_path, branch).text
        return jsonify({'message': commit_message, 'status': 'success'})
    except Exception as e:
        return jsonify({'message': str(e), 'status': 'error'})

@app.route('/generate_summary', methods=['POST'])
def generate_summary():
    repo_path = request.form.get('repo_path')
    branch = request.form.get('branch') or 'main'
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    
    try:
        summary = generate_commit_summary(repo_path, start_date, end_date, branch)
        return jsonify({'message': summary, 'status': 'success'})
    except Exception as e:
        return jsonify({'message': str(e), 'status': 'error'})

if __name__ == '__main__':
    app.run(debug=True)