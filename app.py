from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# from .csv
df = pd.read_csv('data.csv')

@app.route('/')
def index():
    # unique names and dates from drop menu
    names = df['name'].unique()
    dates = df['date'].unique()
    return render_template('index.html', names=names, dates=dates, result=None)

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    date = request.form['date']
    # searching by name and date
    row = df[(df['name'] == name) & (df['date'] == date)]
    if not row.empty:
        shift = row['shift'].values[0]
        type_ = row['type'].values[0]
        result = f"Shift: {shift}, Type: {type_}"
    else:
        result = "Data not found"
    # unique names and dates from drop menu
    names = df['name'].unique()
    dates = df['date'].unique()
    return render_template('index.html', names=names, dates=dates, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
