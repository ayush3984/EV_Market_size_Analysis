# 🚗 Electric Vehicle Market Size Analysis

This project analyzes the growth, distribution, and future market trends of Electric Vehicles (EVs) using Python and real-world EV registration data.

> **Tech stack:** Python, Pandas, NumPy, Matplotlib, Seaborn, SciPy, Jupyter Notebook

---

## 📌 Project Overview

The goal of this project is to:

- Understand how EV adoption has changed over time.
- Study which regions and manufacturers dominate the EV market.
- Analyze EV range capabilities.
- Estimate **future EV market size (2024–2029)** using an exponential growth model.

This repository is ideal as a **data analysis / data science portfolio project**.

---

## 📂 Project Structure

```text
EV_Market_Size_Analysis/
│
├── analysis.ipynb                 # Main Jupyter Notebook with full analysis
├── main.py                        # (Optional) Script version of the analysis
├── Electric_Vehicle_Population_Data.csv   # Dataset used in the analysis
├── images/                        # Exported plots used in the README
│   ├── ev_adoption_trend.png
│   ├── ev_type_distribution.png
│   ├── ev_manufacturers.png
│   ├── ev_range_distribution.png
│   └── ev_market_forecast.png
└── README.md
🧮 Data & Preprocessing
The dataset contains detailed information about registered EVs:

Model year

Make & model

Electric vehicle type (BEV / PHEV)

Electric range

Location (county, city), etc.

Basic preprocessing steps:

Loading data with Pandas

Inspecting columns and data types

Dropping rows with missing critical values

Preparing data for aggregation and visualization

python
Copy code
import pandas as pd

df = pd.read_csv("Electric_Vehicle_Population_Data.csv")
df = df.dropna()
📈 Key Visualizations
1️⃣ EV Adoption Over Time
This plot shows how EV registrations have grown by model year.


2️⃣ EV Type Distribution (BEV vs PHEV)
This visualization compares the popularity of Battery Electric Vehicles (BEV) vs Plug-in Hybrid Electric Vehicles (PHEV).


3️⃣ Top Manufacturers
This bar chart highlights the top EV manufacturers based on number of vehicles registered.


4️⃣ Electric Range Distribution
This chart shows how EV electric range (in miles) is distributed across vehicles in the dataset.


🔮 Market Size Forecast (2024–2029)
Using historical registration data, an exponential growth model is fitted:

𝑦
=
𝑎
⋅
𝑒
𝑏
𝑥
y=a⋅e 
bx
 
Where:

𝑥
x = year index

𝑦
y = number of registrations

𝑎
,
𝑏
a,b = parameters estimated using scipy.optimize.curve_fit

The model is then used to forecast the number of EV registrations from 2024 to 2029.


This gives an approximate future trend assuming current growth patterns continue.

⚙️ How to Run the Project Locally
Clone the repository:

bash
Copy code
git clone https://github.com/ayush3984/EV_Market_Size_Analysis.git
cd EV_Market_Size_Analysis
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
venv\Scripts\activate      # On Windows
Install dependencies:

bash
Copy code
pip install pandas numpy matplotlib seaborn scipy notebook
Start Jupyter Notebook:

bash
Copy code
jupyter notebook
Open analysis.ipynb and run all cells.

📊 Skills Demonstrated
Data cleaning & preprocessing with Pandas

Exploratory data analysis (EDA)

Data visualization with Matplotlib and Seaborn

Basic time-series style analysis

Curve fitting / forecasting with SciPy

Organizing and documenting a project in GitHub

🚀 Future Improvements
Some ideas to extend this project:

Use more advanced forecasting models (ARIMA, Prophet, etc.)

Include charging infrastructure data (charging stations, locations)

Compare EV adoption across multiple states / countries

Build a small dashboard (Streamlit / Plotly Dash) for interactive exploration

👤 Author
Ayush

GitHub: @ayush3984

Feel free to open an issue or reach out if you have suggestions or feedback!

yaml
Copy code

4. Scroll down → **Commit changes**.

Your README will now display all images beautifully.

---

## 4️⃣ If images don’t show up

Check:

- The filenames in `images/` exactly match what you used in the README (case-sensitive).
- Example: if the file is `EV_Adoption_Trend.PNG`, rename it to `ev_adoption_trend.png` to match the README.

---

If you want next, I can:

- Help you **write a short project description for your resume/linkedin**  
- Or help you create **another data project** that pairs well with this one.
::contentReference[oaicite:0]{index=0}






