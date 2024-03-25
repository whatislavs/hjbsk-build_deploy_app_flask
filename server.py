from flask import Flask, render_template, request
from Maths.mathematics import summation, substraction, multiplication
# Import the Maths package here

app = Flask("Mathematics Problem Solver")

@app.route("/sum")
def sum_route():
    if(request.args.get('num1') and request.args.get('num2')):
        try:
            num1 = float(request.args.get('num1'))
            num2 = float(request.args.get('num2'))
        except ValueError:
            return "Provide a numerical value"
        return str(summation(num1, num2))
    return "No value provided"

@app.route("/sub")
def sub_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    return str(substraction(num1, num2))

@app.route("/mul")
def mul_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    return str(multiplication(num1, num2))

@app.route("/")
def render_index_page():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)
