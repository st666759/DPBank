from flask import Flask, render_template
import ngrok

app = Flask(__name__)

@app.route('/')
def index():
     return render_template('main.html')

@app.route('/login')
def login():
     return render_template('login.html')


if __name__ == '__main__':
    app.run(debug= True, port = 5000)
