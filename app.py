from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    # prints
    return 'test'

@app.route('/post', methods=['POST'])
def hello():
    json = request.get_json()
    print(json)
    return 'code'
    

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80)