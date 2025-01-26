from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": 'Tom'},
    {"id": 2, "name": "Jerry"},
    {"id": 3, "name": "Bugs Bunny"}
]

@app.route('/example')
def home():
    return "Welcome to the Flask API!"

@app.route('/', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/<int:id>', methods=['GET'])
def get_student_by_id(id):
    student = next((s for s in students if s["id"] == id), None)
    return jsonify(student) if student else (jsonify({"error": "Student not found"}), 404)

@app.route('/', methods=['POST'])
def add_student():
    new_student = request.get_json()
    if "id" not in new_student or "name" not in new_student:
        return jsonify({"error": "Invalid data"}), 400
    students.append(new_student)
    return jsonify(new_student), 201

@app.route('/<int:id>', methods=['PUT'])
def update_student(id):
    updated_data = request.get_json()
    student = next((s for s in students if s["id"] == id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    student["name"] = updated_data.get("name", student["name"])
    return jsonify(student)

@app.route('/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [s for s in students if s["id"] != id]
    return jsonify({"message": "Student deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
