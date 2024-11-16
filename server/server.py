from flask import Flask,render_template, request, jsonify
# from werkzeug.utils import secure_filename
# import cv2
# import numpy as np
import util

app = Flask(__name__, static_folder='../client', template_folder='../client')

@app.route('/')
def index():
    return render_template('app.html')

@app.route('/predict_disease', methods=['POST'])
def predict_disease():
    try:
        # Parse the incoming JSON data
        data = request.get_json()

        # Check if the data is None or empty (useful for debugging)
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400

        # Extract values from the incoming JSON object
        jaundice = data.get('jaundice')
        fatigue = data.get('fatigue')
        discomfort = data.get('discomfort')
        appetite = data.get('appetite')
        urine = data.get('urine')
        itchy_skin = data.get('itchySkin')
        bruising = data.get('bruising')
        nausea_vomiting = data.get('nauseaVomiting')
        smoking_status = data.get('smokingStatus')
        alcohol_consumption = data.get('alcoholConsumption')

        # Check if any required field is missing
        if None in ([jaundice, fatigue, discomfort, appetite, urine, itchy_skin, bruising, nausea_vomiting, smoking_status, alcohol_consumption]):
            return jsonify({'error': 'Missing required fields'}), 400

        # Predict the disease using your utility function
        predicted_disease = util.predict_disease(
            jaundice, fatigue, discomfort, appetite, urine, itchy_skin,
            bruising, nausea_vomiting, smoking_status, alcohol_consumption
        )

        # Return the prediction as JSON
        print(predict_disease)
        response = jsonify({
            'estimated_disease': predicted_disease
        })
        if(predict_disease):
            print("Danger!!!!")
        else:
            print("Safeee :)")
        response.headers.add('Access-Control-Allow-Origin', '*')  # Add CORS headers if needed
        return response

    except Exception as e:
        # Handle errors in case of unexpected issues
        print(e)
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# @app.route('/predict_image_disease', methods=['POST'])
# def predict_image_disease():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'})
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'})
#     if file:
#         filename = secure_filename(file.filename)
#         # Save the uploaded file to a folder
#         file.save(filename)
#         # Read the saved image
#         # image = cv2.imread(filename)
#         # Call the function from util to predict using CNN model
#         # predicted_result = util.predict_image_disease(image)
#         return jsonify({'predicted_result': predicted_result})

if __name__ == "__main__":
    print("Starting Python Flask server for Disease Prediction...")
    util.load_saved_models()
    app.run()
