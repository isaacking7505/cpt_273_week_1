
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



'''

Please create 4 API endpoints

GET /   - Gets all Students as JSON
GET /<id> - gets student by ID as JSON object
POST / - Add NEW student to the array above and returns 200 "added" if added
PUT /<id> - Updates name of student given an ID
DELETE /<id> - Deletes student from array by given ID

Once your API has been created and tested, please publish it to GitHub and submit the URL of the public repository to Brightspace!

'''




if __name__ == '__main__':
    app.run(debug=True)