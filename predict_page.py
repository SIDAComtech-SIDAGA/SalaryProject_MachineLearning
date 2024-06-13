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
    st.write("""We need some information to predict the salary""")
 