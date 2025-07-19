#!/bin/bash
cd /home/site/wwwroot
export FLASK_APP=your_flask_app.py
gunicorn --bind 0.0.0.0:5000 wsgi:app
