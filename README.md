# Barcode Project

This project is a web application designed to generate unique barcodes for each registered user for event entry. The application includes features for user registration, login, and barcode generation. Additionally, it provides an interface for administrators to scan barcodes for entry validation.

## Features

- User registration with unique number generation
- Login system with password hashing
- Barcode generation for each registered user
- Interface for barcode scanning
- Administrator panel to view user database

## Technologies Used

- Flask
- SQLite
- Jinja2 for templating
- WTForms for form handling
- Werkzeug for password hashing
- Barcode library for generating barcodes

## Installation and Setup

### Prerequisites

- Python 3.6 or higher
- Git

### Local Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/barcode_project.git
    cd barcode_project
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Initialize the database:

    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. Run the application:

    ```bash
    flask run
    ```

6. Open your browser and navigate to `http://127.0.0.1:5000`.

### Deployment on PythonAnywhere

1. Sign in to your [PythonAnywhere](https://www.pythonanywhere.com) account. If you don't have an account, create one.

2. Open a Bash console from the Dashboard.

3. Clone your repository on PythonAnywhere:

    ```bash
    git clone https://github.com/yourusername/barcode_project.git
    cd barcode_project
    ```

4. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

5. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Configure the web app:
    - Go to the Web tab.
    - Click on "Add a new web app".
    - Follow the prompts to configure the app, choose Flask as the framework, and select the correct Python version.

7. Configure the WSGI file:
    - Go to the Web tab and find your web app.
    - Click on "WSGI configuration file".
    - Edit the file to point to your Flask app:

    ```python
    import sys
    import os

    # Add your project directory to the sys.path
    project_home = '/home/yourusername/barcode_project'
    if project_home not in sys.path:
        sys.path = [project_home] + sys.path

    # Set the virtualenv directory
    activate_this = os.path.expanduser("~/<your-virtualenv>/bin/activate_this.py")
    with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))

    # Set the Flask app environment variable
    os.environ['FLASK_APP'] = 'app.py'

    # Import your application
    from app import app as application
    ```

8. Reload the web app from the Web tab.

9. Open your web app URL provided by PythonAnywhere to access your deployed application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [SQLite](https://www.sqlite.org/)
- [PythonAnywhere](https://www.pythonanywhere.com/)
