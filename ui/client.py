from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

ip = '172.16.40.149'
port = 5009

@app.route("/")
def index():
    return render_template("client.html",ipaddress=ip,port=port)

if __name__ == "__main__":
    app.run()