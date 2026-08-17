
import streamlit as st
import pandas as pd

# Base URL of the Flask backend
BACKEND_URL = "https://backend:7860"

# Set the title of the Streamlit app
st.title("SuperKart Sales Prediction App")

# Section for online prediction
st.subheader("Online Prediction")

# Input fields for product and store data
Product_Weight = st.number_input("Product Weight", min_value=0.0, value=12.66)
Product_Sugar_Content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
Product_Allocated_Area = st.number_input("Product Allocated Area (linear in.)", min_value=0.0, value=100.0)
Product_MRP = st.number_input("Maximum Retail Price (USD)", min_value=0.0, value=150.0)
Store_Size = st.selectbox("Store Size", ["Small", "Medium", "High"])
Store_Location_City_Type = st.selectbox("Store Location City Type", ["Tier 1", "Tier 2", "Tier 3"])
Store_Type = st.selectbox("Store Type", ["Supermarket Type1", "Supermarket Type2", "Departmental Store", "Food Mart"])
Product_Id_char = st.selectbox("Product Id Prefix", ["FD", "NC", "DR"])
Product_Type_Category = st.selectbox("Product Type Category", ["Perishables", "Non Perishables"])

product_data = {
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_MRP": Product_MRP,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "Product_Id_char": Product_Id_char,
    "Product_Type_Category": Product_Type_Category
}

if st.button("Predict", type='primary'):
  try:
    response = requests.post(f"{BACKEND_URL}/v1/sales", json=product_data)    # Complete the code to enter user name and space name to correctly define the endpoint
    if response.status_code == 200:
        result = response.json()
        predicted_sales = result["Predicted Sales"]
        st.write(f"Predicted Product Store Sales Total: ₹{predicted_sales:.2f}")
    else:
        st.error("Error in API request")
  except Exception as e:
    st.error(f"Error in API request. Error message:{e}")
