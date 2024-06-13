import streamlit  as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        Data = pickle.load(file)
    return Data

Data = load_model()
gressor_Loaded = Data["model"]
Le_Country = Data["Le_Country"]
Le_Education = Data["Le_Education"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")
    
    st.write("""### We need some information to predict the salary""")
    
    Countries = (
    "United States of America",
            "Germany",
            "United Kingdom of Great Britain and Northern Ireland",
            "Canada",
            "India",
            "France",
            "Netherlands",
            "Australia",
            "Brazil",
            "Spain",
            "Sweden",
            "Italy",
            "Poland",
            "Switzerland",
            "Denmark",
            "Norway",
            "Israel"
        )
    Edications = (
            'Bachelor’s degree',
            'Less than a Bachelors',
            'Master’s degree',
            'Post grad'
        )
    Country = st.selectbox("Country", Countries)
    Education = st.selectbox("Education Level", Edications)
    Experience = st.slider("Years Of Experience",0,50,1)