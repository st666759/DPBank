from flask import Flask, render_template
from pipmysql import connect;


app = Flask(__name__)

connection = connect(
    host = 'localhost', port = port, timeout
)

@app.route('/')
def index():
    return  render_template('index.html');

if __name__ == '__main__':
    app.run(debug = True , port= 5000)

