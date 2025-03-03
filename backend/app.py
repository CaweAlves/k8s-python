import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting_message = os.getenv('GREETING_MESSAGE', 'Hello, World from Backend!')
    return greeting_message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
