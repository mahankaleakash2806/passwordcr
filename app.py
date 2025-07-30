#from utils import lookup
from flask import Flask, render_template, request, redirect, url_for, flash
from hash_crackers import crack_md5, crack_sha1, crack_sha256, crack_bcrypt, crack_argon2, crack_pbkdf2
from utils.cracker import crack_password
import os
import tempfile

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure key in production
UPLOAD_FOLDER = "dictionaries"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle form submission for cracking password
        target_hash = request.form.get("hash") or request.form.get("hash_value")
        algorithm = request.form.get("algorithm") or request.form.get("hash_type")
        wordlist_file = request.files.get("wordlist") or request.files.get("dictionary")

        if not target_hash or not algorithm:
            flash("Hash and algorithm are required.")
            return redirect(url_for("index"))

        wordlist = []
        if wordlist_file and wordlist_file.filename != "":
            # Save uploaded wordlist file temporarily
            temp_path = os.path.join(tempfile.gettempdir(), wordlist_file.filename)
            wordlist_file.save(temp_path)
            # Use crack_password from utils.cracker if available
            password = crack_password(target_hash, algorithm, temp_path)
            os.remove(temp_path)
        else:
            # Use default small wordlist if none uploaded
            wordlist = ['password', '123456', 'admin', 'letmein', 'welcome', 'qwerty']
            if algorithm == 'md5':
                password = crack_md5(target_hash, wordlist)
            elif algorithm == 'sha1':
                password = crack_sha1(target_hash, wordlist)
            elif algorithm == 'sha256':
                password = crack_sha256(target_hash, wordlist)
            elif algorithm == 'bcrypt':
                password = crack_bcrypt(target_hash, wordlist)
            elif algorithm == 'argon2':
                password = crack_argon2(target_hash, wordlist)
            elif algorithm == 'pbkdf2':
                password = crack_pbkdf2(target_hash, wordlist)
            else:
                flash("Unsupported algorithm selected.")
                return redirect(url_for("index"))

        return render_template("results.html", password=password)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
