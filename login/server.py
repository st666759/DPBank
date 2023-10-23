from flask import Flask

app = Flask(__name__)

@app.route('/DPBank_Server')
def start():
    return print('server acces'), 200

if __name__ == '__namme__':
    app.run(host= 'DPBank_Server' , port= 5000);