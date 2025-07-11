from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    expression = data.get('expression', '')

    try:
        # Replace custom symbols with Python-safe expressions
        expression = expression.replace('^', '**')
        expression = expression.replace('π', str(math.pi)).replace('e', str(math.e))
        expression = expression.replace('sqrt', 'math.sqrt')
        expression = expression.replace('log', 'math.log')
        expression = expression.replace('sin', 'math.sin')
        expression = expression.replace('cos', 'math.cos')
        expression = expression.replace('tan', 'math.tan')
        expression = expression.replace('exp', 'math.exp')

        # Safely evaluate expression
        result = eval(expression, {'math': math})
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'result': 'Error'})

if __name__ == '__main__':
    app.run(debug=True)
