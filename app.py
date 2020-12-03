from flask import Flask, request, jsonify

app = Flask(__name__)

#Sample data
data = [
    {
        'Id': 1,
        'BookName': 'Book1',
        'Author': 'Author1'
    }
]

@app.route('/', methods=['GET'])
def home():
    return '''<center><h1>API Hosting in Python'''

@app.route('/data', methods=['GET'])
def displaydata():
    return jsonify(data)

@app.route('/search', methods=['GET'])
def searchbook():
    response = 'Work in Progress'

    if 'id' in request.args:
        # return 'Id found - '+str(request.args['id'])
        searchid = int(request.args['id'])
        # print(searchid)
    else:
        return 'Id not found'

    # print(data[0]['Id'])
    if searchid == data[0]['Id']:
        response='Book Found'
    else:
        response='Requested Book with ID is not found.'

    return response

if __name__ == '__main__':
    app.run(debug=True)
