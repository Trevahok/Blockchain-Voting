from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

ip = 'localhost'
port = 5001

@app.route("/")
def index():
    return render_template("client.html",ipaddress=ip,port=port)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5010)