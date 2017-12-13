from flask import Flask, render_template, request, redirect
import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello"


@app.route('/request-counter', methods=['GET','PUT','DELETE','POST'])
def count():
    data_manager.increase_count(request.method)
    return redirect('/')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
