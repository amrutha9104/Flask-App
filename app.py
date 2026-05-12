from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# Initialize Database
from models import db
from models.student import Student
# Import Routes
from routes.student_routes import student_bp
# Initialize Flask App
app = Flask(__name__)

# Configure Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db.init_app(app)
# Register Blueprint
app.register_blueprint(student_bp)

# Home Route
@app.route('/')
def home():
    students = Student.query.all()
    return render_template('index.html', students=students)

# Create Database Tables
with app.app_context():
    db.create_all()

# Run Application
if __name__ == '__main__':
    app.run(debug=True)
