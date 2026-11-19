# Lagos House Price Predictor

A Streamlit app for exploring estimated residential property prices in Lagos, Nigeria. Choose a property and area to get a model-based estimate for yearly rent, a house sale, or land.

## Live app

Try the app here: [Lagos House Price Predictor](https://lekki-house-price-m4tz5etwyoh5t6nthpqbwr.streamlit.app/)

## What it predicts

- **Yearly rent:** area, bedroom count, property type, and whether the property is a mini flat, newly built/serviced, or furnished.
- **House sale price:** area, bedroom count, property type, and whether the property is a mini flat.
- **Land sale price:** area.

Predictions are estimates from trained models, not property valuations or guaranteed market prices. The displayed “realistic range” is a simple 30% band around the estimate, not a statistical confidence interval. The land estimate is area-based and does not account for plot size.

## Run locally

Use Python 3.9 or newer. From the project directory, install the dependencies and start Streamlit:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

The app opens in your browser, usually at `http://localhost:8501`.

## Project files

- `app.py` — Streamlit interface and prediction logic.
- `rent_model.pkl`, `rent_feature_cols.pkl` — rent model and its expected input features.
- `sale_house_model.pkl`, `sale_house_cols.pkl` — house sale model and its expected input features.
- `sale_land_model.pkl`, `sale_land_cols.pkl` — land sale model and its expected input features.
- `Data/` — source and cleaned property listing datasets.
- `Notebook/` — notebooks used to explore the data and develop the prediction models.
- `requirements.txt` — Python package dependencies.

The serialized model files must be present in the project directory for the app to start. Only use model files from a trusted source.
