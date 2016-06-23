from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)


@app.route('/')
def calculator():
    return render_template('index.html')


@app.route('/calc.py', methods=['POST'])
def calculator_post():
    error = ''
    number_one = request.form['first-number']
    if number_one.isdigit():
        number_one = float(number_one)
    else:
        error = 'First number is not a digit'
        return render_template('index.html', result='', error=error)
    number_two = request.form['second-number']
    if number_two.isdigit():
        number_two = float(number_two)
    else:
        error = 'Second number is not a digit'
        return render_template('index.html', result='', error=error)
    operator = request.form['operation']
    if operator not in ['+', '-', '/', '*']:
        error = 'Invalid operation'
        return render_template('index.html', result='', error=error)


    def add(a, b):
        return a + b


    def multiply(a, b):
        return a * b


    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'You cannot divide by 0'


    def substract(a, b):
        return a - b


    actions = {
        '+': add,
        '*': multiply,
        '/': divide,
        '-': substract
        }


    result = actions[operator](number_one, number_two)

    return render_template('index.html', result=result, error=error)


if __name__ == '__main__':
    app.run()
