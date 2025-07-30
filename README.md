
# Universal Hash Password Cracker

## Project Description
This is a Flask-based web application designed to crack hashed passwords using various hashing algorithms. Users can input a hash value, select the hashing algorithm used, and optionally upload a custom wordlist to attempt to crack the password. The application supports multiple popular hashing algorithms and provides a simple web interface for ease of use.

## Features
- Supports cracking of the following hash algorithms:
  - MD5
  - SHA1
  - SHA256
  - Bcrypt
  - Argon2
  - PBKDF2
- Option to upload a custom wordlist file for password cracking.
- Default small wordlist included for quick testing.
- Simple and clean web interface using Flask and HTML templates.
- Displays cracked password or failure message clearly.

## Installation
1. Clone the repository.
2. Ensure Python 3.x is installed.
3. Install required dependencies:
   ```
   pip install flask bcrypt argon2-cffi passlib
   ```
4. Run the application:
   ```
   python app.py
   ```

## Usage
1. Open your web browser and navigate to `http://127.0.0.1:5000/`.
2. Enter the hash value you want to crack.
3. Select the hash algorithm used to generate the hash.
4. (Optional) Upload a custom wordlist file (.txt) to use for cracking.
5. Click "Crack Password" to start the cracking process.
6. View the results on the results page.

## File Structure
- `app.py`: Main Flask application handling routes and logic.
- `hash_crackers.py`: Contains functions to crack hashes for supported algorithms.
- `utils/cracker.py`: Placeholder for cracking logic with uploaded wordlists.
- `wordlist.py`: Utility script to generate a sample wordlist file.
- `templates/`: HTML templates for the web interface.
  - `index.html`: Form for inputting hash and options.
  - `results.html`: Displays cracking results.
- `static/css/style.css`: Stylesheet for the web interface.
- `README.md`: Project documentation.

## Notes
- The current implementation of `utils/cracker.py` contains a placeholder function for cracking with uploaded wordlists.
- Default wordlist used if no custom wordlist is uploaded includes common passwords like "password", "123456", etc.
- Replace the `app.secret_key` in `app.py` with a secure key for production use.

## License
This project is open source and free to use.
