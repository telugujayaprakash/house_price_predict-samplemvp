from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import traceback

app = Flask(__name__)
CORS(app)

try:
    # Try to load the model and handle any loading errors
    model = joblib.load("house_price_model.pkl")
except Exception as e:
    print("Error loading model:", e)
    traceback.print_exc()
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received data:", data)
        print("Data types:", [type(feature) for feature in data['features']])  # Log the types
        
        # Ensure features are in the correct format
        features = [float(feature) for feature in data['features']]
        prediction = model.predict([features])
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        print("Prediction error:", e)
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
