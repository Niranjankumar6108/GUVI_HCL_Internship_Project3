from flask import Flask, request, render_template
import pickle
import json
import numpy as np

app = Flask(__name__)

# Load model and columns
model = pickle.load(open('model.pickle', 'rb'))
with open('columns.json', 'r') as f:
    data_columns = json.load(f)['data_columns']  # includes sqft, bath, bhk + locations

# Extract locations (columns from index 3 onwards)
locations = data_columns[3:]

@app.route('/')
def home():
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        sqft = float(request.form['sqft'])
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])
        location = request.form['location']

        # Create feature vector
        x = np.zeros(len(data_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk

        if location.lower() in locations:
            loc_index = locations.index(location.lower()) + 3  # +3 because first 3 are sqft, bath, bhk
            x[loc_index] = 1

        estimated_price = model.predict([x])[0]
        prediction_text = f"Estimated Price: {round(estimated_price, 2)} Lakh"

    except Exception as e:
        prediction_text = f"Error: {str(e)}"

    return render_template('index.html', prediction_text=prediction_text, locations=locations)


if __name__ == "__main__":
    app.run(debug=True)
