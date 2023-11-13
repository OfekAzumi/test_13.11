from flask import Flask, jsonify, render_template, request
from project.numbers.simp import Adding,Subtracting
from project.numbers.comp import SumOfDigits,isPal
from col import myZip

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/functions", methods=['POST'])
def math():
    data = request.json
    n1 = data.get('n1')
    n2 = data.get('n2')
    func = data.get('func')
    calls = data.get('call')


    if not n1 and not n2:
        return jsonify({'error': 'Data is Required'}), 404
    
    # if n2 is missing, use functions
    if not n2:
        if not n1:
            return jsonify({'error': 'Number 1 is Required'}), 404
        if (calls == False):
            return jsonify({'error': 'You need to call add/subtract funtions first'}), 404
        # if function is sum all digits
        if (func == "sum"):
            return jsonify({'message': f'{SumOfDigits(int(n1))}'}), 200
        # if function is palindrom
        if (func == "pal"):
            return jsonify({'message': f'{isPal(int(n1))}'}), 200
    
    # if there are 2 numbers, but the function needs 1
    if func == "sum" or func == "pal" and n1 and n2: 
        return jsonify({'error': 'You need to enter number 1, not number 2'}), 404
    
    # if n2, but not n1 - missing data
    if n2 and not n1:
        return jsonify({'error': 'You need to enter number 1, not number 2'}), 404
    
    # if function is sum all digits
    if (func == "add"):
        return jsonify({'message': f'{Adding(int(n1),int(n2))}'}), 200
    # if function is palindrom
    if (func == "sub"):
        return jsonify({'message': f'{Subtracting(int(n1),int(n2))}'}), 200


if __name__ == "__main__":
    app.run(debug=True)