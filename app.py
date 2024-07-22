from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the scaler and model
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)
with open('adam_nn.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

house_mapping = {
    1: 'Ravenclaw',
    2: 'Slytherin',
    3: 'Gryffindor',
    4: 'Hufflepuff'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [
        int(data['friends']),
        1 if data['leadership'] == 'Yes' else 0,
        data['hobbies'],
        data['inasis']
    ]
    
    # Transform categorical variables
    hobbies_mapping = {
        'physical': 0, 
        'creative': 1, 
        'cerebral': 2, 
        'making-tinkering': 3, 
        'community-activities': 4, 
        'collecting': 5
    }
    inasis_mapping = {
        'MAYBANK': 0, 
        'PROTON': 1, 
        'TRADEWINDS': 2, 
        'MAS': 3, 
        'TNB': 4, 
        'YAB': 5, 
        'MUAMALAT': 6, 
        'BSN': 7, 
        'TM': 8, 
        'BANK ISLAM': 9, 
        'SIME DARBY': 10, 
        'PETRONAS': 11, 
        'SME': 12, 
        'PERSISIRAN SINTOK': 13, 
        'TAMAN UNI': 14
    }

    features[2] = hobbies_mapping[features[2]]
    features[3] = inasis_mapping[features[3]]
    
    # Scale the features
    features = np.array(features).reshape(1, -1)
    features_scaled = scaler.transform(features)
    
    # Predict
    prediction=model.predict(features_scaled)
    prediction_int=int(prediction[0])
    house_name=house_mapping[prediction_int]
    return jsonify({'prediction':house_name})

if __name__ == '__main__':
    app.run(debug=True)
