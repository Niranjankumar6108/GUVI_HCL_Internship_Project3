# 🏡 Bangalore Home Price Prediction

This project is a **Flask web application** that predicts the price of houses in Bangalore based on:
- Area (Square Feet)
- Number of Bedrooms (BHK)
- Number of Bathrooms
- Location

The model is trained using Linear Regression with one-hot encoded location data.

---

## 🚀 Features
- Simple web interface with form inputs
- Dynamic location dropdown populated from `columns.json`
- Automatic one-hot encoding of location
- Real-time price prediction
- Flask backend + HTML/CSS frontend

---

## 📂 Project Structure

GUVI_HCL_Internship_Project3
│

├── Bangalore-Home-Price-Prediction.ipynb  # Jupyter Notebook with complete code

├── app.py # Flask backend

├── model.pickle # Trained Machine Learning model

├── columns.json # Contains feature names (sqft, bath, bhk, locations)

├── templates/
│ └── index.html # Frontend HTML template

├── requirements.txt # Python dependencies

└── README.md # Project documentation


---

## 🛠 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Niranjankumar6108/GUVI_HCL_Internship_Project3.git
   cd GUVI_HCL_Internship_Project3

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv venv
     source venv/bin/activate    # On Linux/Mac
     venv\Scripts\activate       # On Windows

3. **requirements.txt**
   ```bash
   Python 3.8+
   Flask
   scikit-learn
   numpy

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt

## ▶️ Run the App
    python app.py
    
    The app will start at:
    
    👉 http://127.0.0.1:5000/

## 📊 Input Example
    Area (Square Feet): 1000
    BHK: 2
    Bath: 2
    Location: 1St Phase Jp Nagar

## Output:
    Estimated Price: 83.87 Lakh

<img width="943" height="815" alt="image" src="https://github.com/user-attachments/assets/75a62fc5-c510-417d-be87-fcaa874c198f" />

