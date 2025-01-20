
# Flask Library
from flask import Flask


# Create App Object
app = Flask(__name__)


# List of Students
students = [
    {
        "id": 1,
        "name": 'tom'
    },
    {
        "id": 2,
        "name": "Jerry"
    },
    {
        "id": 3,
        "name": "Bugs Bunny"
    }
]

# Example endpoint
@app.route('/example')
def home():
    return "Welcome to the Flask API!"

#### ASSIGNMENT STARTS HERE ####





#### ASSIGNMENT ENDS HERE ####

if __name__ == '__main__':
    app.run(debug=True)
