from flask import Blueprint, jsonify, redirect, request, url_for
from models import db
from models.student import Student

# Create Blueprint
student_bp = Blueprint('student_bp', __name__)

# GET All Students
@student_bp.route('/students', methods=['GET'])
def get_students():

    students = Student.query.all()

    return jsonify([
        student.to_dict() for student in students
    ])

# CREATE 
@student_bp.route('/students/add', methods=['GET'])
def add_student():

    name = request.args.get('name')
    age = request.args.get('age')

    if not name or not age:
        return jsonify({
            'message': 'Please provide both name and age in the URL'
        }), 400

    student = Student(
        name=name,
        age=age
    )

    db.session.add(student)
    db.session.commit()

    # if request.headers.get('Accept', '').find('text/html') != -1:
    #     return redirect(url_for('home'))

    return jsonify({
        'message': 'Student added successfully'
    })
