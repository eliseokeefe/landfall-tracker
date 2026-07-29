from flask import Flask, jsonify, send_from_directory
from parser import is_landfall  # imports landfall function 
#flask server that shows landfall data via api/landfalls and serves the frontend files 
app = Flask(__name__)

already_load = False #global variable reset to false on rerun
data = None 

@app.route("/api/landfalls")
def landfalls():
    global already_load, data #declare global variables within the method
    if(already_load): #if the data has already been parsed, return the existing data cache
        return data 
    else: #if the data hasn't been cached, run is_landfall, save the data cache to the global variable, and set the already_loaded variable to true so the code knows the data has been cached
        data = jsonify(is_landfall())
        already_load = True 
        return data 

@app.route("/")
def home(): #utilize html page for user interface 
    return send_from_directory(".", "interface.html")

@app.route("/<path:filename>") #catches requests from other files, like the CSS or JS, and serves it directly from the same folder as app.py
def static_files(filename):
    return send_from_directory(".", filename)

if __name__ == "__main__": #set the port number and only runs the code if the file is executed directly, not when imported
    app.run(debug=True, port=8000)