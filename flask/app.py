# api.py
#1. generates web interface index.html
#2. gets user input from index.html
#3. uses function in api.py to calculate presidents most similar to user input
#4. sends list of similar presidents back to user at index.html


from flask import Flask, make_response, request, abort, jsonify, render_template
from api import get_similar_presidents

app = Flask(__name__)
app.debug = True

@app.route('/similar_presidents', methods=['POST'])
def get_score():

    if not request.json or  ('president' not in request.json):
        abort(400)


    president = request.json['president']


    score = get_similar_presidents(president,3)

    response = {

        'score': score
    }
    print('score =')
    print(score)
    return jsonify(response), 201

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
