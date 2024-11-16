import json
import pickle
import numpy as np

__model = None
__data_columns = 10
# __cnn_model = None

# for predicting disease
def predict_disease(jaundice, fatigue, discomfort, appetite, urine, itchy_skin, bruising, nausea_vomiting, smoking_status, alcohol_consumption):
    try:
        global __data_columns
        x = np.zeros(len(__data_columns))
        x[0] = jaundice
        x[1] = fatigue
        x[2] = discomfort
        x[3] = alcohol_consumption
        x[4] = smoking_status
        x[5] = appetite
        x[6] = urine
        x[7] = itchy_skin
        x[8] = bruising
        x[9] = nausea_vomiting
        return round(__model.predict([x])[0],2)
    except Exception as e:
        print(e)
        return "Error occurred while predicting liver disease."

# for loading the saved models
def load_saved_models():
    global __model
    global __data_columns
    # global __cnn_model
    
    with open("./model/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

    with open("./model/liver_disease_prediction.pickle", "rb") as f:
        __model = pickle.load(f)
        
    # Load CNN model
    # __cnn_model = load_cnn_model("./model/cnn_model.pickle")

# def load_cnn_model(model_path):
#     with open(model_path, 'rb') as f:
#         model = pickle.load(f)
#     return model

# # Function to predict from the CNN model
# def predict_image_disease(image):
#     try:
#         # Preprocess the image if required
#         # Example: resizing, normalization, etc.
#         # Perform prediction
#         # Assuming you have a function predict_cnn(image) to predict from CNN model
#         predicted_result = predict_cnn(image)
#         return predicted_result
#     except Exception as e:
#         return f"Error occurred while predicting from CNN model: {str(e)}"



# main function
if __name__ == "__main__":
    load_saved_models()
    print(predict_disease(1, 1, 1, 1, 1, 1, 1, 1, 0, 2))