import os
from dotenv import load_dotenv
import subprocess
import google.generativeai as genai
import argparse

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GOOGLE_MODEL_NAME = os.getenv('GOOGLE_MODEL_NAME')
REPOS_BASE_PATH = '/repos'

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(GOOGLE_MODEL_NAME)

def get_current_branch():
    result = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], 
                          capture_output=True, text=True)
    return result.stdout.strip()

def get_git_changes(repo_path=None, branch=None):
    if repo_path:
        # Handle both absolute paths and relative paths within REPOS_BASE_PATH
        if not repo_path.startswith('/'):
            repo_path = os.path.join(REPOS_BASE_PATH, repo_path)
        
        if not os.path.exists(repo_path):
            raise ValueError(f"Repository path not found: {repo_path}")
            
        os.chdir(repo_path)
    
    if branch is None:
        branch = get_current_branch()
    
    # Get staged changes
    staged_changes = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True).stdout
    
    # Get unstaged changes
    unstaged_changes = subprocess.run(["git", "diff"], capture_output=True, text=True).stdout
    
    # Get untracked files
    untracked = subprocess.run(["git", "ls-files", "--others", "--exclude-standard"], 
                                capture_output=True, text=True).stdout
    
    # Get branch differences
    branch_diff = subprocess.run(["git", "diff", branch], capture_output=True, text=True).stdout
    
    return {
        'staged': staged_changes,
        'unstaged': unstaged_changes,
        'untracked': untracked,
        'branch_diff': branch_diff
    }

def generate_commit_message(repo_path=None, branch=None):
    changes = get_git_changes(repo_path, branch)
    current_branch = get_current_branch()
    
    prompt = f"""You are an expert at creating detailed github commit messages.
    Generate a comprehensive commit message based on the following changes:
    
    Current Branch: {current_branch}
    
    Staged Changes:
    {changes['staged']}
    
    Unstaged Changes:
    {changes['unstaged']}
    
    Untracked Files:
    {changes['untracked']}
    
    Differences from {branch if branch else current_branch} branch:
    {changes['branch_diff']}
    
    Format the commit message following these rules:
    1. Start with a concise summary line
    2. Add a blank line
    3. Add detailed bullet points of changes
    4. Mention any breaking changes
    5. Reference related issues if detected in the changes
    """
    
    return model.generate_content(prompt)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate detailed commit messages for git changes')
    parser.add_argument('--path', type=str, help='Path to git repository')
    parser.add_argument('--branch', type=str, help='Branch to compare against (defaults to current branch)')
    args = parser.parse_args()
    
    print(generate_commit_message(args.path, args.branch).text)