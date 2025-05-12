from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__, static_folder="static", template_folder="templates")

# Load the trained model and scalers
model = pickle.load(open("model.pkl", "rb"))
minmax_scaler = pickle.load(open("minmaxscaler.pkl", "rb"))
standard_scaler = pickle.load(open("standardscaler.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        N = float(data['N'])
        P = float(data['P'])
        K = float(data['K'])
        temperature = float(data['temperature'])
        humidity = float(data['humidity'])
        ph = float(data['ph'])
        rainfall = float(data['rainfall'])

        # Prepare input data for prediction
        features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        features = minmax_scaler.transform(features)
        features = standard_scaler.transform(features)
        prediction = model.predict(features)[0]

        return jsonify({'recommended_crop': int(prediction)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask App is Running!"

if __name__ == '__main__':
    app.run(debug=True)
