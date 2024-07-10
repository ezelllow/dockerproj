from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<!DOCTYPEHTML> <head><style>body{background-color: blue;}</style></head><html><body><p>Hello, World!</p></body></html>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)