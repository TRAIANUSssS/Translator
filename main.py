from googletrans import *
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def translater():
    translator = Translator()

    if request.method == 'POST':
        trans = request.form.get('trans')  # запрос к данным формы
        lang = request.form.get('lang')
        translation = translator.translate(trans, dest=lang)
        translated_message = translation.text
        return render_template('index.html', my_string=translated_message)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()