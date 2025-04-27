# commiter-ai

This project demonstrates how to use Google's Gemini generative AI model to enhance git workflows within a Flask web application. It provides two main tools:

1. **Commit Message Generator** - Creates tailored git commit messages based on your repository changes
2. **Commit Summary Generator** - Produces comprehensive summaries of commit activity over a specified time period

## Google AI Studio API Key

To use this project, you'll need to obtain an API key from Google AI Studio. Follow these steps:
1. **Go to the <a href="https://aistudio.google.com/plan_information">Google AI Studio API Key page</a>.**
2. **Click on the "Create API Key" button.**
3. **Copy the API key and paste it into the `.env` file.**
4. **Save the `.env` file.**

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/wiIIiams-c/commiter-ai.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd commiter-ai
   ```
3. **Create and populate the .env file:**
   ```bash
   cp .env.template .env
   ```
4. **Environment variables:**
   ```
   GOOGLE_API_KEY=your_google_api_key
   GOOGLE_MODEL_NAME=your_model_name
   REPO_PROJECTS_PATH=/base/path/to/your-projects

   eg: /home/user/projects/hello-world you just only need /home/user/projects
   ```
5. **Install dependencies using pip:**
   ```bash
   pip install -r requirements.txt
   ```
6. **(Optional) Using Docker:**
   * Build the Docker image:
       ```bash
       docker-compose build
       ```
   * Run the Docker container:
       ```bash
       docker-compose up
       ```

## Usage

1. **Run the Flask app:**
   ```bash
   python app.py
   ```
   or if using Docker: Access the application through the port exposed in your `docker-compose.yml` file (default is usually `5000`).

2. **Access the web interface:** Open your browser and go to `http://127.0.0.1:5000/`

3. **Choose a tool:**
   * **Commit Message Generator** - Creates detailed commit messages based on your repository changes
   * **Commit Summary Generator** - Produces summaries of commit activity over a date range

4. **For the Commit Message Generator:**
   * Enter your repository path:
     * If using Docker: `/repos/your-project-folder`
     * If not using Docker: `/full/path/to/your-project`
   * Enter branch name (defaults to 'main')
   * Click "Generate Commit Message"

5. **For the Commit Summary Generator:**
   * Enter your repository path
   * Enter branch name (defaults to 'main')
   * Select a date range
   * Click "Generate Commit Summary"

## Command Line Usage

Both tools can also be used directly from the command line:

1. **Commit Message Generator:**
   ```bash
   python commiter_ai.py --path /path/to/repo --branch your-branch
   ```

2. **Commit Summary Generator:**
   ```bash
   python commit_summary.py --path /path/to/repo --start 2023-01-01 --end 2023-12-31 --branch your-branch
   ```

## Project Structure

```
commiter-ai/
├── templates/
│   ├── index.html
│   ├── commit_generator.html
│   └── commit_summary.html
├── .dockerignore
├── .env.template
├── .gitignore
├── Dockerfile
├── app.py
├── commiter_ai.py
├── commit_summary.py
├── docker-compose.yml
└── requirements.txt
```

* **`templates/index.html`**: Main landing page with links to both tools
* **`templates/commit_generator.html`**: UI for the commit message generator
* **`templates/commit_summary.html`**: UI for the commit summary generator
* **`.dockerignore`**: Specifies files and directories to exclude from the Docker image
* **`.env.template`**: Template for the environment variables file
* **`.gitignore`**: Specifies files and directories to exclude from git tracking
* **`Dockerfile`**: Instructions for building the Docker image
* **`app.py`**: The main Flask application file
* **`commiter_ai.py`**: Contains the logic for generating commit messages
* **`commit_summary.py`**: Contains the logic for generating commit summaries
* **`docker-compose.yml`**: Docker Compose configuration for running the application within a container
* **`requirements.txt`**: Lists the project dependencies

## Features

* **Commit Message Generator:**
  * Analyzes staged changes, unstaged changes, and untracked files
  * Compares changes with a specified branch
  * Generates detailed, structured commit messages
  * Output is in Chilean Spanish by default

* **Commit Summary Generator:**
  * Analyzes commit history over a specified date range
  * Identifies main themes and accomplishments
  * Groups related changes together
  * Highlights major features and technical improvements
  * Output is in Chilean Spanish by default

## Dependencies

* `google-generativeai`
* `python-dotenv`
* `flask`

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

This project is licensed under the [MIT License](LICENSE).
```