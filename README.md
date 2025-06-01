
CROP RECOMMENDATION SYSTEM..!

[Crop_Recommendation_README.1.docx](https://github.com/user-attachments/files/20540197/Crop_Recommendation_README.1.docx)


🌾 Crop Recommendation System

A smart machine learning–based web application that recommends the most suitable crop to grow based on soil and weather conditions.
Built as a final-year major project, this system uses real-world agricultural data to assist farmers, students, and researchers 
in precision farming.


 Project Objective
 

To build an end-to-end crop recommendation system using machine learning that:

- Predicts the best crop to grow using environmental factors
- Provides an easy-to-use web interface built with Streamlit
- Can be deployed and shared via GitHub and Streamlit Cloud

Dataset

-  Name: Crop_recommendation.csv
-  Records: 2200 rows × 8 columns
-  Features:
  - N, P, K — Nitrogen, Phosphorus, Potassium levels in soil
  - temperature, humidity, ph, rainfall — Environmental factors
  - label — Target crop to be predicted (e.g., rice, maize, apple,Coffee)


 
Tech Stack

 Layer                  Tool / Language     

 ML Model          Random Forest Classifier (sklearn) 
 Frontend           Streamlit           
 Data Prep          Pandas, Seaborn, Numpy     
 Environment   Google Colab + Python 
 Deployment     Streamlit Cloud / Localhost 
 Versioning       Git & GitHub   


 ML Workflow

1. Data preprocessing:

   - pH categorized as Acidic / Neutral / Basic
   - Rainfall bucketed as Low / Medium / High (for analysis)
   - No missing values or duplicates

3. Model building:
   
   - Label encoding used on crop names
   - Trained using RandomForestClassifier with 99.3% accuracy
   - Saved using joblib (rf_crop_model.pkl & label_encoder.pkl)




5. Evaluation:
   
- Classification report

  ![image](https://github.com/user-attachments/assets/93012122-1f2c-4251-bee9-7fa01d6ad248)

 
- Confusion matrix visualization
  
  ![Screenshot 2025-05-29 124745](https://github.com/user-attachments/assets/b30a429c-e564-40c3-8c23-cf5674f44186)

 

How to Run This Project Locally

1. Clone this repository

    git clone https://github.com/Jack-tech32/crop-recommendation-system.git
    cd crop-recommendation-system

2. Install required packages

    pip install -r requirements.txt

3. Add model files
    - rf_crop_model.pkl
    - label_encoder.pkl

4. Run the Streamlit app

    streamlit run app.py

 Deploy on Streamlit Cloud :
App Link :-  https://crop-recommendation-system-kwzkgofvhjdkcxzqp5wmuw.streamlit.app/


 App Sample 

![image](https://github.com/user-attachments/assets/a755ea58-569c-4b60-8d71-5434e29fb271)
                   

Author :
Your Name : Jayesh Sanjay Patil  / Username :  Jack-tech32
Final Year B.Tech Student (Data Science)  
Crop Recommendation System – Major Project

Acknowledgements :

- Dataset from Kaggle 
- Built using Streamlit, Scikit-learn, and Python  
- Special thanks to professors, mentors & peers for support

