from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, my name is ABDIFATAH SOANE AHMED, Registration Number: 23/07836 BSD"

# Remove app.run() since Vercel handles the server
