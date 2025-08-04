from flask import Flask
lemon = Flask(__name__)
@lemon.route('/')
def home():
    return "Hello from Azure Flask!"

if __name__ == '__main__':
    lemon.run(host='0.0.0.0', port=8000)
