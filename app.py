from flask import Flask, request, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Load data from the CSV file
df = pd.read_csv('data.csv')

@app.route('/')
def index():
    # Get unique names and dates for dropdown lists
    names = df['name'].unique()
    dates = df['date'].unique()
    return render_template('index.html', names=names, dates=dates)

@app.route('/result', methods=['POST'])
def result():
    # Retrieve name and date from the form data
    name = request.form['name']
    date = request.form['date']
    # Search for the row by name and date
    row = df[(df['name'] == name) & (df['date'] == date)]
    if not row.empty:
        # If data is found, extract shift and type values
        shift = row['shift'].values[0]
        type_ = row['type'].values[0]
        # Return the data as JSON
        return jsonify({'shift': shift, 'type': type_})
    else:
        # If data is not found, return an error message as JSON
        return jsonify({'error': 'Data not found'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
