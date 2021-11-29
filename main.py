from googletrans import *
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def translater():
    native = ''
    trans = ''
    lang = ''
    lang_edited = ''
    translated_message = ''
    code_dict = {'1': 'ru', '2': 'en', '3': 'es', '4': 'fr', '5': 'de'}

    translator = Translator()

    if request.method == 'POST':
        trans = request.form.get('trans')  # запрос к данным формы
        lang = request.form.get('lang')
        print(trans, code_dict[lang])
        if lang in code_dict.keys():
            lang_edited = code_dict[lang]
            translation = translator.translate(trans, dest=lang_edited)
            translated_message = translation.text
            return render_template('index.html', my_string=translated_message)

    return render_template('index.html')



#output: 'The sky is blue and I like bananas'

if __name__ == '__main__':
    app.run(port=3000)