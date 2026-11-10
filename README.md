# Lagos House Price Prediction

A Streamlit app for predicting yearly rent in Lagos from property area, bedroom count, and property features.

## Run the app

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

The app loads the trained model from `rent_model.pkl` and its feature names from `rent_feature_cols.pkl`.

## Project contents

- `app.py` - Streamlit rent prediction interface
- `Data/` - rental and sale listing datasets
- `Notebook/` - model exploration and training notebook
- `rent_model.pkl`, `rent_feature_cols.pkl` - trained model artifacts

The CSV datasets contain property listing details, including addresses.
