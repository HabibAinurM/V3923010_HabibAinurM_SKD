from flask import Flask, render_template, request

app = Flask(__name__)

def cipher(char, key):
    if char.isalpha():
        nilai = ord('A' if char.isupper() else 'a')
        ch = ord(char)
        mod = (ch + key - nilai) % 26
        hasil = chr(mod + nilai)
        return hasil
    else:
        return char

def enkripsi(input_text, key):
    output = ""
    for char in input_text:
        output += cipher(char, key)
    return output

def dekripsi(input_text, key):
    return enkripsi(input_text, 26 - key)

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = None
    text = None
    key = None

    if request.method == 'POST':
        text = request.form['plain']
        key = int(request.form['key'])

        if 'enkripsi' in request.form:
            hasil = enkripsi(text, key)
        elif 'dekripsi' in request.form:
            hasil = dekripsi(text, key)

    return render_template('index.html', hasil=hasil, text=text, key=key)

if __name__ == '__main__':
    app.run(debug=True)
