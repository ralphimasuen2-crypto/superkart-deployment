
import streamlit as st
import pandas as pd
import requests

# Base URL of the Flask Backend
BACKEND_URL = "http://backend:7860"

# Page title
st.title("SuperKart Sales System")
st.write("Enter the product and store details below to predict the total sales.")

# Input fields for product and store data
Product_Weight = st.number_input("Product Weight", min_value=0.0, value=12.66)
Product_Sugar_Content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"] )
Product_Allocated_Area = st.number_input("Product Allocated Area",min_value=0.0, value=0.027)
Product_MRP = st.number_input("Product MRP", min_value=0.0, value=117.08)
Store_Size = st.selectbox("Store Size", ["Small", "Medium", "Large"])
Store_Location_City_Type = st.selectbox("Store Location City Type", ["Tier 1", "Tier 2", "Tier 3"])
Store_Type = st.selectbox("Store_Type", ["SupermarketType1", "SupermarketType2", "SupermarketType3" "Departmental Store", "Food Mart"])
Product_Id_Char = st.selectbox("Product ID Character" ["FD", "DR", "NC"])
Store_Age_Years = st.number_input("Store Age (Years)", min_value=0.0, value=16)
Product_Type_Category = st.selectbox("Product Type Category", ["Perishables", "Non Perishables"])

# Create JSON payload
payload = {
    "Product_Weight": Product_Weight,
    "Product _Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_MRP": Product_MRP,
    "Store_Size": Store_Size,
    "Store_Location_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "Product_Id_Char": Product_Id_Char,
    "Store_Age_Years": Store_Age_Years,
    "Product_Type_Category": Product_Type_Category,
}

# Single Prediction
if st.button("Predict", type="primary"):
    response = requests.post(f"{BACKEND_URL}/v1/predict", json=product_data
    )
    if response.status_code==200:
      result=response.json()
      predicted_sales = result["Sales"]
      st.success(f"Predicted Product Store Sales Total: {predicted_sales:.2f}")
    else:
      st.error("Unable to connect to the prediction API.")

# Batch Prediction
st.subheader("Batch Prediction")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    if st.button("Predict for Batch", type="primary"):

        response = requests.post(f"{BACKEND_URL}/v1/predictbatch", files={"file":uploaded_file})
        if response.status_code == 200:
            result = response.json()
            st.success("Prediction completed successful!")
            try:
                if isinstance(results, list):
                    df=pd.DataFrame(results)
                elif isinstance(results, dict):
                     # check if all values are scaler
                     if all(not isinstance(v, (list, dict)) for v in results.values()):
                         df=pd.DataFrame([results])
                     else:
                         df=pd.DataFrame(result)
                else:
                     df=pd.DataFrame({"Result": [results]})

                     st.dataframe(df, use_container_width=True)

            except Exception as e:
                st.error(f"Unable to display results as in table: {e}")
                st.json(result)

        else:
            st.error("Unable to connect to the prediction API.")
