from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Flask!'

@app.route('/fbnq')
def fbnq():
    num = int(request.args.get('num', '10'))
    first = 1
    second = 1
    third = 0
    count = 3
    if num == 1 or num == 2 :
        return str(1)
    else:
        while count < num:
            third = first + second
            first = second
            second = third
            count = count + 1
        return str(third)

if __name__ == '__main__':
    app.run()