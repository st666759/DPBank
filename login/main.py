from flask import Flask

app = Flask(__name__)

@app.route('/DPBank_Server')
def index():
    return render_template('index.html')

if __name__ ==  '__name__':
    app.run(host= 'DPBank Server', port= 5000);