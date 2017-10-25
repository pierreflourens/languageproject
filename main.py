from flask import Flask, request
from models import PierreWord
app = Flask(__name__)


@app.route('/create_word')
def create_word():
    english = request.args.get('english')
    french = request.args.get('french')
    spanish = request.args.get('spanish')

    new_word = PierreWord()
    new_word.english = english
    new_word.french = french
    new_word.spanish = spanish

    new_word.put()

    return 'you can see your word here: http://127.0.0.1:8080/get_word?english=' + english, 200


@app.route('/get_word')
def get_word():
    word = request.args.get('english')
    #blablabla

    word_object = PierreWord.query(PierreWord.english==word).get()

    return word_object.spanish, 200


if __name__ == '__main__':
    app.run()
