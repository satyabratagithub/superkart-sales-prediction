
import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, jsonify

# Initialize Flask app
superkart_app = Flask("SuperKart Sales Predictor")


# Load the trained machine learning model
model = joblib.load("superkart_forecast_model_v1_0.joblib")

# Define a route for the home page (GET request)
@superkart_app.get('/')
def home():
    """
    This function handles GET requests to the root URL ('/') of the API.
    It returns a simple welcome message.
    """
    return "Welcome to the SuperKart Sales Predictor APP!"


# Define an endpoint for single sales prediction (POST request)
@superkart_app.post('/v1/sales')
def predict_rental_price():
  try:
    """
    This function handles POST requests to the '/v1/sales' endpoint.
    It expects a JSON payload containing products and store details and returns
    the predicted net sales as a JSON response.
    """
    # Get the JSON data from the request body
    sales_data = request.get_json()
    print("Raw incoming data:", sales_data)

    # Extract relevant features from the JSON data
    sample = {
          'Product_Weight': float(sales_data['Product_Weight']),
          'Product_Sugar_Content': sales_data['Product_Sugar_Content'],
          'Product_Allocated_Area': float(sales_data['Product_Allocated_Area']),
          'Product_MRP': float(sales_data['Product_MRP']),
          'Store_Size': sales_data['Store_Size'],
          'Store_Location_City_Type': sales_data['Store_Location_City_Type'],
          'Store_Type': sales_data['Store_Type'],
          'Product_Id_char': sales_data['Product_Id_char'],
          'Product_Type_Category': sales_data['Product_Type_Category']
     }

    # Convert the extracted data into a Pandas DataFrame
    input_data = pd.DataFrame([sample])

    # Make prediction
    predicted_sales = model.predict(input_data)[0]

    # Round predicted_sales to two decimal places
    predicted_sales = round(float(predicted_sales), 2)

    # Return the actual price
    return jsonify({'Predicted Sales': predicted_sales})
  except Exception as e:
    return jsonify({'Prediction Failed due to ': str(e)}), 500

# Run the Flask application in debug mode if this script is executed directly
if __name__ == '__main__':
    superkart_app.run(debug=True)
