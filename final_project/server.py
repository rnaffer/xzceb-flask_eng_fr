from machinetranslation import translator
from flask import Flask, render_template, request
import json
from translator import english_to_french, french_to_english

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    text_to_translate = request.args.get('textToTranslate')

    return english_to_french(text_to_translate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    text_to_translate = request.args.get('textToTranslate')

    return french_to_english(text_to_translate)

@app.route("/")
def renderIndexPage():
    return render_template('templates/index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
