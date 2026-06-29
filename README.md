# Employee Attrition Prediction 🚀

Predict which employees will leave your company with 87% accuracy!

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![XGBoost](https://img.shields.io/badge/ML-XGBoost-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

---

## 📋 What is This?

A machine learning system that predicts employee attrition (employees leaving) before it happens. Companies can then take action to keep important employees.

### Why Use This?
- 💰 Save ₹2-10 lakhs per employee by preventing turnover
- 📊 Identify at-risk employees automatically
- 🎯 Take action BEFORE they leave
- 📈 87% prediction accuracy

---

## 🎯 Quick Start

### 1. Install
```bash
git clone https://github.com/YOUR-USERNAME/employee-attrition.git
cd employee-attrition
pip install -r requirements.txt
```

### 2. Run the App
```bash
streamlit run app/streamlit_app.py
```

### 3. Make a Prediction
- Enter employee details
- Click "Predict"
- See if they will leave or stay!

---

## 📊 How Good is It?

| Metric | Score |
|--------|-------|
| Accuracy | 87% ✅ |
| Precision | 79% ✅ |
| Recall | 72% ✅ |
| F1-Score | 75% ✅ |

---

## 🔑 What Causes Attrition?

Top reasons employees leave:

```
1. Low Salary              (18.5%) 💰
2. Low Job Satisfaction   (16.2%) 😞
3. Too Much Work          (14.8%) 😫
4. New Employee           (11.3%) 🆕
5. Poor Work-Life Balance  (9.7%) ⚠️
```

---

## 📁 Files Included

```
employee-attrition/
├── app/                    # Web app files
│   ├── streamlit_app.py   # Main app
│   └── model_predictor.py # Predictions
├── models/                 # Trained models
│   └── xgboost_model.pkl  # Our best model
├── data/                   # Datasets
│   ├── raw/               # Original data
│   └── processed/         # Cleaned data
├── notebooks/              # Python notebooks
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_model.ipynb
│   └── 04_evaluation.ipynb
└── README.md              # This file
```

---

## 💻 How to Use

### Web Interface (Easy)
```bash
streamlit run app/streamlit_app.py
# Open http://localhost:8501
# Fill in employee info
# See prediction!
```

### Python Code
```python
import joblib
import pandas as pd

# Load model
model = joblib.load('models/xgboost_model.pkl')

# Employee data
employee = pd.DataFrame({
    'MonthlyIncome': [4_50_000],
    'JobSatisfaction': [2],
    'OverTime': [1],
    'YearsAtCompany': [2],
    'WorkLifeBalance': [2],
    'Age': [28],
    'DistanceFromHome': [45],
    'Department_IT': [0],
    'Department_Sales': [1],
    'Department_HR': [0]
})

# Predict
prob = model.predict_proba(employee)[0][1]
print(f"Will Leave? {prob*100:.1f}%")
```

---

## 📊 Dataset Info

- **Total:** 1,470 employees
- **Attrition Rate:** 16.2% (237 left)
- **Features:** 35 columns
- **Target:** Yes/No (Will they leave?)

### Key Data
```
MonthlyIncome    → Salary (₹)
JobSatisfaction  → 1-4 scale
WorkLifeBalance  → 1-4 scale
YearsAtCompany   → Tenure (years)
Age              → Employee age
Department       → Sales/IT/HR
OverTime         → Yes/No
Attrition        → YES/NO (target)
```

---

## 📈 Example Results

### High Risk ⚠️ (82% will leave)
```
Name: Ravi
Age: 28
Salary: ₹2,80,000 (Low)
Satisfaction: 2/4 (Low)
Years: 1.5 (New)
Work-Life Balance: 2/4 (Poor)

→ HR Should: Offer raise, talk to him, improve role
```

### Medium Risk 🟠 (55% might leave)
```
Name: Priya
Age: 32
Salary: ₹4,20,000 (OK)
Satisfaction: 3/4 (Good)
Years: 4 (Stable)
Work-Life Balance: 3/4 (Good)

→ HR Should: Check in regularly, support career growth
```

### Low Risk ✅ (12% will leave)
```
Name: Ahmed
Age: 45
Salary: ₹6,50,000 (High)
Satisfaction: 4/4 (Excellent)
Years: 10 (Very loyal)
Work-Life Balance: 4/4 (Excellent)

→ HR Should: Keep as mentor, leadership role
```

---

## 🛠️ Technologies

```
Python Libraries:
├── pandas          # Data handling
├── numpy           # Math operations
├── scikit-learn    # ML tools
├── xgboost         # Our model
├── streamlit       # Web app
├── matplotlib      # Charts
└── seaborn         # Better charts

Tools:
├── Jupyter Notebook # Code & analysis
├── Git             # Version control
└── GitHub          # Repository
```

---

## 🔍 Model Details

### We Tried:
- Logistic Regression (78% accurate)
- Decision Tree (82% accurate)
- Random Forest (84% accurate)
- **XGBoost (87% accurate)** ⭐ BEST!

### Why XGBoost?
- Best accuracy (87%)
- Handles complex patterns
- Robust to outliers
- Great for business use

---

## 📊 Key Findings

### By Department
```
Sales:  20.6% leave (Highest) 🔴
IT:     13.8% leave           🟠
HR:      6.3% leave (Lowest)  🟢
```

### By Age
```
18-25: 25% leave (Young, mobile)
26-35: 15% leave
36-45: 10% leave
45+:    5% leave (Stable, experienced)
```

### By Salary
```
< ₹2,50,000:       28% leave (High risk)
₹2,50,000-5,00,000: 15% leave (Medium)
> ₹5,00,000:         7% leave (Low risk)
```

### By Satisfaction
```
Low (1/4):       31% leave (DANGER!)
Medium (2/4):    12% leave
High (3/4):       6% leave
Very High (4/4):  2% leave (SAFE!)
```

---

## 💡 What HR Should Do

### High Risk Employees (>70% chance)
✅ Meet with employee  
✅ Understand their problems  
✅ Offer salary increase  
✅ Discuss promotion  
✅ Improve their role  
✅ Flexible work options  

### Medium Risk (40-70% chance)
✅ Regular check-ins  
✅ Career planning  
✅ Training programs  
✅ Mentorship  
✅ Support & feedback  

### Low Risk (<40% chance)
✅ Annual reviews  
✅ Leadership roles  
✅ Skill development  
✅ Keep motivated  

---

## 📉 Business Value

### Without Prediction
```
100 employees
↓
15 leave per year
↓
Cost: ₹30-120 lakhs
```

### With Our Model
```
100 employees
↓
Identify 15 at-risk
↓
Keep 9-10 of them
↓
Save: ₹18-72 lakhs per year
```

---

## 🚀 How to Deploy

### Local Computer
```bash
streamlit run app/streamlit_app.py
```

### Cloud (Streamlit Cloud)
```bash
# Push to GitHub
git push origin main

# Go to: https://streamlit.io/cloud
# Click: "New app"
# Choose your repo
# Select: app/streamlit_app.py
# Deploy!
```

### Other Cloud Options
- AWS
- Google Cloud
- Heroku
- Azure

---

## 📚 Project Structure Explained

```
📊 data/
   raw/           → Original data file
   processed/     → Cleaned & ready data

📓 notebooks/
   01_eda         → Explore the data (charts, trends)
   02_prep        → Clean & prepare data
   03_model       → Build & train model
   04_eval        → Check accuracy & results

🤖 models/
   xgboost.pkl    → Saved model (can predict now!)
   scaler.pkl     → Data converter

🌐 app/
   streamlit_app.py  → Web interface code
   model_predictor.py → Prediction logic
```

---

## ⚙️ Install Requirements

```bash
pip install streamlit==1.28.0
pip install pandas==2.0.0
pip install numpy==1.24.0
pip install scikit-learn==1.3.0
pip install xgboost==2.0.0
pip install joblib==1.3.0
pip install matplotlib==3.7.0
pip install seaborn==0.12.0
pip install plotly==5.17.0
```

Or simply:
```bash
pip install -r requirements.txt
```

---

## 🆘 Troubleshooting

### Problem: "Module not found"
```bash
pip install -r requirements.txt
```

### Problem: "Model file not found"
```bash
# Retrain the model
python notebooks/03_model_building.ipynb
```

### Problem: "Port already in use"
```bash
streamlit run app/streamlit_app.py --server.port 8502
```

### Problem: "Data file not found"
```bash
# Check file path in app
# Make sure data/ folder exists
```

---

## 📖 Learn More

### About Attrition
- [SHRM - Employee Turnover](https://www.shrm.org)
- [HBR - Retention Strategies](https://hbr.org)

### About Machine Learning
- [XGBoost Docs](https://xgboost.readthedocs.io)
- [Scikit-learn Guide](https://scikit-learn.org)
- [Pandas Tutorial](https://pandas.pydata.org)

### About Deployment
- [Streamlit Docs](https://docs.streamlit.io)
- [Streamlit Cloud](https://streamlit.io/cloud)

---

## 🤝 Want to Contribute?

1. Fork this repo
2. Make a branch: `git checkout -b feature/your-idea`
3. Make changes
4. Commit: `git commit -m "Your message"`
5. Push: `git push origin feature/your-idea`
6. Create Pull Request

### Ideas to Add:
- Better visualizations
- New models
- API endpoint
- Mobile app
- More datasets
- Better documentation

---

## 📄 License

MIT License - Free to use and modify!

---

## 👤 Author

**Aafreen**
- GitHub: [@Aafreenhaq2105](https://github.com/Aafreenhaq2105)
- Kaggle: [@aafreenhaq](https://kaggle.com/aafreenhaq)
- Email: aafreen@example.com

---

## ⭐ Support

If this helped you, please:
- ⭐ Star this repo on GitHub
- 🔗 Share with others
- 💬 Give feedback
- 🐛 Report bugs

---

## 📊 Project Stats

```
Status:       ✅ Active & Working
Accuracy:     87%
Models:       4 tested, 1 best
Data Points:  1,470 employees
Time to Build: 40+ hours
Ready to Use: YES! 🚀
```

---

<div align="center">

**Made with ❤️ using Python, XGBoost & Streamlit**

[⬆ Back to Top](#employee-attrition-prediction-)

Last Updated: January 2025

</div>
