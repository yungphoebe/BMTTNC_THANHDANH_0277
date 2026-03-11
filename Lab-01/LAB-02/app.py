from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.playfair.playfair_cipher import PlayFairCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.transposition.transposition_cipher import TranspositionCipher
app = Flask(__name__)


# router routes for home page
@app.route("/")
def home():
    return render_template('index.html')


# router routes for caesar cypher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')


@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])

    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)

    return render_template("caesar.html", result_encrypt=encrypted_text)


@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])

    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)

    return render_template("caesar.html", result_decrypt=decrypted_text)

@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']

    vigenere = VigenereCipher()
    encrypted_text = vigenere.vigenere_encrypt(text, key)

    return render_template("vigenere.html", result_encrypt=encrypted_text)

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']

    vigenere = VigenereCipher()
    decrypted_text = vigenere.vigenere_decrypt(text, key)

    return render_template("vigenere.html", result_decrypt=decrypted_text)

@app.route("/playfair")
def playfair():
    return render_template("playfair.html")


@app.route("/playfair/creatematrix", methods=['POST'])
def playfair_creatematrix():
    key = request.form['inputKeyMatrix']

    playfair = PlayFairCipher()
    playfair_matrix = playfair.create_playfair_matrix(key)

    return render_template("playfair.html", playfair_matrix=playfair_matrix)


@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']

    playfair = PlayFairCipher()
    playfair_matrix = playfair.create_playfair_matrix(key)
    encrypted_text = playfair.playfair_encrypt(text, playfair_matrix)

    return render_template("playfair.html", result_encrypt=encrypted_text)


@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']

    playfair = PlayFairCipher()
    playfair_matrix = playfair.create_playfair_matrix(key)
    decrypted_text = playfair.playfair_decrypt(text, playfair_matrix)

    return render_template("playfair.html", result_decrypt=decrypted_text)


@app.route("/railfence")
def railfence():
    return render_template("railfence.html")


@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])

    railfence = RailFenceCipher()
    encrypted_text = railfence.rail_fence_encrypt(text, key)

    return render_template("railfence.html", result_encrypt=encrypted_text)


@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])

    railfence = RailFenceCipher()
    decrypted_text = railfence.rail_fence_decrypt(text, key)

    return render_template("railfence.html", result_decrypt=decrypted_text)

@app.route("/transposition")
def transposition():
    return render_template("transposition.html")


@app.route("/transposition/encrypt", methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])

    transposition = TranspositionCipher()
    encrypted_text = transposition.encrypt(text, key)

    return render_template("transposition.html", result_encrypt=encrypted_text)


@app.route("/transposition/decrypt", methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])

    transposition = TranspositionCipher()
    decrypted_text = transposition.decrypt(text, key)

    return render_template("transposition.html", result_decrypt=decrypted_text)
# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)  