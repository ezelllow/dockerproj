from flask import Flask
import os

app = Flask(__name__)

# Ensure the log directory exists
log_dir = '/mnt/log'
os.makedirs(log_dir, exist_ok=True)

# Create a log file
with open(os.path.join(log_dir, 'app.log'), 'a') as log_file:
    log_file.write("Application started\n")

@app.route('/')
def hello_world():
    return '<!DOCTYPEHTML> <head><style>body{background-color: blue;}</style></head><html><body><p>Hello, World!</p></body></html>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

