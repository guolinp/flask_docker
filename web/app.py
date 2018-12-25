from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)

@app.route("/")
def show_details() :
    return "<html>"   + \
           "<head>"   + \
           "<title>"  + \
           "Flask"    + \
           "</title>" + \
           "</head>"  + \
           "<body>"   + \
           "this is a example of flask docker" + \
           "</body>"  + \
           "</html>"

@app.route("/json")
def send_json() :
    return jsonify( {"A" : "aaa", "B" : "bbb", "C" : "ccc"})

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')
