# commiter-ai

This project demonstrates how to use Google's Gemini generative AI model to create custom git commit messages within a simple Flask web application.  It allows users to input the changes they've made and receive a tailored commit message suggestion.

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
   ```JSON
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

2. **Access the web interface:** Open your browser and go to `http://127.0.0.1:5000/` (or the appropriate port if using Docker).

3. **Enter your project path:**
    * If you are using docker:
        ```bash
        /repos/your-project-folder
        ```
    * If you are not using docker:
        ```bash
        /full/path/to/your-project
        ```

4. **Generate commit message:** Click the "Generate Commit Message" button.

5. **View the suggested commit message:** The generated commit message will be displayed on the page.


## Project Structure

```
commiter-ai/
├── templates/
│   └── index.html
├── .dockerignore
├── .env.template
├── .gitignore
├── Dockerfile
├── app.py
├── commiter_ai.py
├── docker-compose.yml
└── requirements.txt
```

* **`templates/index.html`**: The HTML template for the web interface.
* **`.dockerignore`**: Specifies files and directories to exclude from the Docker image.
* **`.env.template`**: Template for the environment variables file.
* **`.gitignore`**: Specifies files and directories to exclude from git tracking.
* **`Dockerfile`**: Instructions for building the Docker image.
* **`app.py`**: The main Flask application file.
* **`commiter_ai.py`**: Contains the logic for interacting with the Google Gemini API.
* **`docker-compose.yml`**: Docker Compose configuration for running the application within a container.
* **`requirements.txt`**: Lists the project dependencies.


## Dependencies

* `google-generativeai`
* `python-dotenv`
* `flask`


## Contributing

Contributions are welcome!  Please feel free to submit pull requests or open issues.


## License

This project is licensed under the [MIT License](LICENSE). (You would need to create a LICENSE file containing the MIT license text).
```