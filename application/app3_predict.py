from json import load
import streamlit as st
import pickle
import numpy as np
import base64



def load_model():
    with open("saved_pick.pkl", "rb") as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor_loaded = data["model"]
le_region = data["le_region"]
le_sex = data["le_sex"]
LR_model = data["logestic_model"]
scaler = data["scaler_model"]



def show_predict_page():
    def set_bg_hack_url():
        st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://www.oie.int/app/uploads/2021/04/microsoftteams-image-1.jpeg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )



    set_bg_hack_url()


    st.title("Covid-19 Death Prediction Application")
    st.write("Created By: Derek Westjohn and Elizabeth Severance")
    st.write("""### Features For Predicting Death Probability """)

    years = (
    "2020",
    "2021"    
    )

    months = (
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9", 
    "10",
    "11",
    "12")

    regions = (
    "Southern",
    "North West",
    "South West",
    "Pacific Coastal",
    "Rocky Mountains",
    "New England",
    "Mid Atlantic",
    "Oceanic",
    "Mid West",
    "Caribbean"
    )

    sexes = (
    "Male",
    "Female"
    )


    years = st.selectbox("Year", years)
    months = st.selectbox("Month", months)
    regions = st.selectbox("Region", regions)
    sexes = st.selectbox("Sex", sexes)

    age = st.slider("Age", 0, 90, 30, step=10)

    ok = st.button("Calculate Death Probability")

    if ok:
        X = np.array([[years, months, regions, sexes, age]])
        X[:, 2] = le_region.transform(X[:, 2])
        X[:, 3] = le_sex.transform(X[:, 3])
        X = X.astype(float)
        X_scaled = scaler.transform(X)

        # deaths = regressor_loaded.predict(X)
        lr_deaths = LR_model.predict_proba(X_scaled)
        # st.subheader(f"The estimated deaths: {deaths[0]:.0f}")
        st.subheader(f"Based on the selected features above: ")
        st.subheader(f"The probability of living from Covid-19: {lr_deaths[0,0]:.0%}")
        st.subheader(f"The probability of dying from Covid-19: {lr_deaths[0,1]:.0%}")


   
