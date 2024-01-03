from flask import Flask, request, jsonify, render_template

#Crwate the app object
app = Flask(__name__)

# importing functions for calculations
from bmi_calc_function import bmi_calc

#Define Calculator
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index', methods=['POST'])        #you will have to edit out predict
def index():

    weight = request.form['weight']
    height = request.form['height']
    
    result = bmi_calc(weight, height)

    return render_template('index.html', prediction_text = str(result))

if __name__ == "__main__":
    app.run(debug=True)