from flask import Flask,jsonify
from json import load
with open('valid_aids_file.json', 'r') as aids_file:
    valid_aids = load(aids_file)
app = Flask(__name__)
@app.route('/verify/<int:aid>', methods= ['GET'])
def verify_aadhar(aid):
    return jsonify(
        {
            'valid': aid in valid_aids['aids'],   
        }
    )

if __name__ == '__main__':
    app.run(debug=True)