import os
import sys
import argparse
from datetime import datetime
from dotenv import load_dotenv
import subprocess
import google.generativeai as genai

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GOOGLE_MODEL_NAME = os.getenv('GOOGLE_MODEL_NAME')

if not GOOGLE_API_KEY:
    print("Error: GOOGLE_API_KEY environment variable not set")
    sys.exit(1)

if not GOOGLE_MODEL_NAME:
    print("Error: GOOGLE_MODEL_NAME environment variable not set")
    sys.exit(1)

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(GOOGLE_MODEL_NAME)

def get_commits_in_range(repo_path=None, start_date=None, end_date=None, branch='main'):
    """Get git commits within a specified date range"""
    if repo_path:
        if not os.path.exists(repo_path):
            raise ValueError(f"Repository path not found: {repo_path}")
        os.chdir(repo_path)
    
    date_filter = ""
    if start_date and end_date:
        date_filter = f"--after={start_date} --before={end_date}"
    elif start_date:
        date_filter = f"--after={start_date}"
    elif end_date:
        date_filter = f"--before={end_date}"
    
    # Get commit history with full details
    git_cmd = f"git log {branch} {date_filter} --pretty=format:'%h|%an|%ad|%s' --name-status"
    result = subprocess.run(git_cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise Exception(f"Git command failed: {result.stderr}")
    
    return result.stdout

def generate_commit_summary(repo_path=None, start_date=None, end_date=None, branch='main', prompt_template=None):
    """Generate a summary of Git commits based on a date range"""
    commits = get_commits_in_range(repo_path, start_date, end_date, branch)
    
    if not commits.strip():
        return "No commits found in the specified date range."
    
    default_prompt = f"""You are a technical writer summarizing development work.
    Create a comprehensive summary of the following git commits from {start_date or 'the beginning'} to {end_date or 'now'}:
    
    {commits}
    
    Please provide:
    1. An overview of the main themes and accomplishments
    2. Major features or components that were worked on
    3. Any notable refactoring or technical improvements
    4. Group related changes together in a logical way
    5. Use professional, clear language suitable for a development team or stakeholders
    6. Answer in chilean human spanish language
    
    Format as a well-structured human-readable report with sections and bullet points where appropriate.
    """
    
    prompt = prompt_template if prompt_template else default_prompt
    response = model.generate_content(prompt)
    return response.text

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a summary of git commits within a date range')
    parser.add_argument('--path', type=str, help='Path to git repository')
    parser.add_argument('--start', type=str, help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end', type=str, help='End date (YYYY-MM-DD)')
    parser.add_argument('--branch', type=str, default='main', help='Branch to analyze')
    parser.add_argument('--custom-prompt', type=str, help='Custom prompt template for the AI')
    
    args = parser.parse_args()
    
    try:
        summary = generate_commit_summary(
            args.path, 
            args.start, 
            args.end, 
            args.branch,
            args.custom_prompt
        )
        print(summary)
    except Exception as e:
        print(f"Error generating summary: {e}")
        sys.exit(1) 