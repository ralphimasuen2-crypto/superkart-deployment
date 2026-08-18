
# import necessary libraries
import numpy as np
import joblib # For loading the serialized model
import pandas as pd # For data manipulation
from flask import Flask, request, jsonify # For creating the Flask APIs

# Initialise Flask API with a name
superkart_api = Flask("SuperKart")

# Load the saved model pipeline from the file
model = joblib.load("superkart_model.joblib")

# Define a route for the home page
@superkart_api.get('/')
def home():
  return "Welcome to the SuperKart System"

# Define an Endpoint to predict sales for a single product
@superkart_api.post('/v1/predict')
def predict_sales():
    # Get data from json file
    data = request.get_json()

    # Extract relevant features from the input data
    sample = {
        "Product_Weight": data["Product_Weight"],
        "Product_Sugar_Content": data["Product_Sugar_Content"],
        "Product_Allocated_Area": data["Product_Allocated_Area"],
        "Product_MRP": data["Product_MRP"],
        "Store_Size": data["Store_Size"],
        "Store_Location_City_Type": data["Store_Location_City_Type"],
        "Store_Type": data["Store_Type"],
        "Product_Id_Char": data["Product_Id_Char"],
        "Store_Age_Years": data["Store_Age_Years"],
        "Product_Type_Category": data["Product_Type_Category"],
    }

    # Extract relevant features from the input data
    input_data = pd.DataFrame([sample])

    # Make a prediction using the trained model
    prediction = model.predict(input_data).tolist()[0]

    # Return the prediction as a JSON response
    return jsonify({"Sales": prediction})

    # Define an endpoint to predict sales for a batch of products
    @superkart_api.post('/v1/predictbatch')
    def predict_sales_batch():  
        # Get the uploaded CSV file from the request
        file = request.files['file']

        # Read the file into a DataFrame
        input_data = pd.read_csv(file)
      
        # Make predictions for the batch data
        prediction = model.predict(input_data).tolist()

        # Create an output dictionary mapping row index to predicted sales
        output_dict = {str(i): round(pred, 2) for i, pred in enumerate(prediction)}

        return output_dict

    # Run the Flask app in debug mode
    if __name__ == '__main__':
        superkart_api.run(host="0.0.0.0", port=7860)
