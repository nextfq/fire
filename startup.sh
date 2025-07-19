#!/bin/bash
cd /home/site/wwwroot
export FLASK_APP=your_flask_app.py

# 使用 Gunicorn 绑定到 80 端口
gunicorn --bind 0.0.0.0:80 wsgi:app

# 如果你选择直接使用 Flask 运行，也可以这样做：
#python your_flask_app.py --host=0.0.0.0 --port=80
