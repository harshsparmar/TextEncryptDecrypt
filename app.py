from flask import Flask, render_template, request
import string
import random

app = Flask(__name__)

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

def encrypt_text(text):
    cipher_text = ""
    for letter in text:
        index = chars.index(letter)
        cipher_text += key[index]
    return cipher_text

def decrypt_text(text):
    plain_text = ""
    for letter in text:
        index = key.index(letter)
        plain_text += chars[index]
    return plain_text

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        user_input = request.form['user_input']
        encrypted_text = encrypt_text(user_input)
        return render_template('encrypt.html', user_input=user_input, encrypted_text=encrypted_text)
    return render_template('encrypt.html')

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        user_input = request.form['user_input']
        decrypted_text = decrypt_text(user_input)
        return render_template('decrypt.html', user_input=user_input, decrypted_text=decrypted_text)
    return render_template('decrypt.html')

if __name__ == '__main__':
    app.run(debug=True)
