# House Price Predictor

An AI/ML web app that predicts house prices based on size, bedrooms, and age.

## 🔗 Live App
**[Click Here to Use the App](https://your-streamlit-link-here.streamlit.app/)**


## What It Does
- Enter house details (size in sq ft, number of bedrooms, age in years)
- Model instantly predicts the price
- Shows predicted price in Rupees

## Technology Stack
- Python
- scikit-learn (Linear Regression)
- pandas
- Streamlit
- GitHub

## How It Works
1. Trained on 20 houses with their actual prices
2. Uses Linear Regression algorithm
3. Learns the relationship between features and price
4. Predicts price for new houses

## Model Details
- Algorithm: Linear Regression
- Type: Regression (predicts numerical value)
- Features: 3 house attributes (size, bedrooms, age)
- Average Prediction Error: Rs 1,56,682

## How to Use
1. Open the live app link above
2. Enter house details
3. Click Predict Price
4. Get instant price estimate

## Run Locally
```bash
git clone https://github.com/Aafreenhaq2105/house-price-predictor.git
cd house-price-predictor
pip install -r requirements.txt
python train.py
streamlit run app.py
```

## Project Files
- `app.py` - Streamlit web application
- `train.py` - Model training code
- `data.csv` - Training data
- `model.pkl` - Trained model
- `requirements.txt` - Dependencies

## Skills Demonstrated
✅ Machine Learning Regression
✅ Python Programming
✅ Web App Development (Streamlit)
✅ Model Deployment
✅ GitHub & Git

## Status
✅ Complete and Live
