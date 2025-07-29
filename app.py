from flask import Flask, render_template, request, redirect, url_for, flash
import os
from hash_crackers import crack_md5, crack_sha1, crack_sha256, crack_bcrypt, crack_argon2, crack_pbkdf2
import tempfile

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure key in production

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crack', methods=['POST'])
def crack():
    target_hash = request.form.get('hash')
    algorithm = request.form.get('algorithm')
    wordlist_file = request.files.get('wordlist')

    if not target_hash or not algorithm:
        flash('Hash and algorithm are required.')
        return redirect(url_for('index'))

    wordlist = []
    if wordlist_file and wordlist_file.filename != '':
        # Read uploaded wordlist file
        wordlist = [line.strip() for line in wordlist_file.stream.read().decode('utf-8', errors='ignore').splitlines() if line.strip()]
    else:
        # Use a default small wordlist if none uploaded
        wordlist = ['password', '123456', 'admin', 'letmein', 'welcome', 'qwerty']

    password = None
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
        flash('Unsupported algorithm selected.')
        return redirect(url_for('index'))

    return render_template('results.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
