# Flask Student App

This is a simple Flask project for managing student data.

## Features

- View all students
- Add a student
- Store data using SQLite
- Return student data as JSON

## Project Structure

```text
Flask-App/
|-- app.py
|-- requirements.txt
|-- models/
|   |-- __init__.py
|   `-- student.py
|-- routes/
|   `-- student_routes.py
|-- templates/
|   `-- index.html
`-- static/
    `-- style.css
```

## Installation

1. Create a virtual environment:

```bash
python -m venv venv
```

2. Activate the virtual environment:

```bash
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

```bash
python app.py
```

The app will run locally at:

```text
http://127.0.0.1:5000/
```

## Routes

- `/` : Home page
- `/students` : Get all students in JSON format
- `/students/add?name=John&age=20` : Add a new student

## Database

The project uses SQLite and automatically creates a `students.db` file when the app starts.
