from flask import Flask, jsonify, send_from_directory
from parser import is_landfall  # imports landfall function 

app = Flask(__name__)

already_load = False 
data = None 

@app.route("/api/landfalls")
def landfalls():
    global already_load, data 
    if(already_load):
        return data 
    else: 
        data = jsonify(is_landfall())
        already_load = True 
        return data 

@app.route("/")
def home():
    return send_from_directory(".", "interface.html")

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(".", filename)

if __name__ == "__main__":
    app.run(debug=True, port=8000)