from utils import lookup

from flask import Flask, render_template, request
from utils.cracker import crack_password
import os

app = Flask(__name__)
UPLOAD_FOLDER = "dictionaries"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        hash_value = request.form["hash_value"]
        hash_type = request.form["hash_type"]
        dict_file = request.files["dictionary"]
        dict_path = os.path.join(app.config["UPLOAD_FOLDER"], dict_file.filename)
        dict_file.save(dict_path)
        result = crack_password(hash_value, hash_type, dict_path)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
