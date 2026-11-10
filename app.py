# app.py - Lagos Rent Predictor
import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('rent_model.pkl','rb'))
cols = pickle.load(open('rent_feature_cols.pkl','rb'))

st.title("🏠 Lagos Rent Predictor")
st.write("Predict yearly rent for Lagos based on Area, Bedrooms, Type")

area = st.selectbox("Area", sorted([c.replace('area_','') for c in cols if c.startswith('area_')]))
bedrooms = st.slider("Bedrooms", 0, 6, 2)
prop_type = st.selectbox("Property Type", sorted([c.replace('prop_type_','') for c in cols if c.startswith('prop_type_')]))
is_mini = st.checkbox("Mini Flat?")
is_new = st.checkbox("Newly Built / Serviced?")
is_furnished = st.checkbox("Furnished?")

if st.button("Predict Rent"):
    row = {c:0 for c in cols}
    row['bedrooms'] = bedrooms
    row['is_mini'] = int(is_mini)
    row['is_new'] = int(is_new)
    row['is_furnished'] = int(is_furnished)
    if f'prop_type_{prop_type}' in row: row[f'prop_type_{prop_type}'] = 1
    if f'area_{area}' in row: row[f'area_{area}'] = 1
    pred = float(np.expm1(model.predict(pd.DataFrame([row])[cols])[0]))
    st.success(f"Predicted Rent: ₦{pred:,.0f} / year")
    st.caption(f"Model Accuracy: R2 0.59 | MAE ₦879k | 57.8% within 30%")
    # Range
    st.info(f"Realistic Range: ₦{pred*0.7:,.0f} - ₦{pred*1.3:,.0f}")