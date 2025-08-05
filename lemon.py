from flask import Flask
lemon = Flask(__name__)

@lemon.route('/')
def home():
    return "Hello, Fucking Azure!"

if __name__ == '__main__':
    lemon.run(host='0.0.0.0', port=8080)  # 🔥Azure  一定要 8080
