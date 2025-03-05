# flask-cloud-app from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, my name is ABDIFATAH SOANE AHMED, Registration Number: 23/07836 BSD"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
