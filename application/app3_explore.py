from matplotlib import patches
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, classification_report
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, train_test_split
from scipy.stats import norm
import pickle

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


def clean_experience(x):
    if x == "Under 1 year":
        return 1
    if x == "0-17 years":
        return 10
    if x == "1-4 years":
        return 10
    if x == "5-14 years":
        return 10
    if x == "15-24 years":
        return 20
    if x == "18-29 years":
        return 20
    if x == "25-34 years":
        return 30
    if x == "30-39 years":
        return 30
    if x == "35-44 years":
        return 40
    if x == "40-49 years":
        return 40
    if x == "45-54 years":
        return 50
    if x == "50-64 years":
        return 50
    if x == "55-64 years":
        return 60
    if x == "65-74 years":
        return 70
    if x == "75-84 years":
        return 80
    if x == "85 years and over":
        return 90
    return float(x)


def data_clean():
    data = pd.read_csv("covid19.csv")
    df = pd.DataFrame(data)
    df = df[["Group", "Year", "Month", "State", "Sex", "Age Group", "COVID-19 Deaths"]]
    df = df.rename({"COVID-19 Deaths": "Deaths"}, axis=1)
    df = df.rename({"Age Group": "Age"}, axis=1)
    df = df[df["Deaths"].notnull()]
    df = df.dropna()
    df = df[df["Group"] == "By Month"]
    df = df.drop("Group", axis=1)
    df.drop(df[df['Sex'] == "All Sexes"].index, inplace = True)
    df.drop(df[df['Age'] == "All Ages"].index, inplace = True)
    df["Age"] = df["Age"].apply(clean_experience)
    df.drop(df[df['State'] == "United States"].index, inplace = True)
    df["State"] = df["State"].replace("Maine", "New England")
    df["State"] = df["State"].replace("Rhode Island", "New England")
    df["State"] = df["State"].replace("Vermont", "New England")
    df["State"] = df["State"].replace("Connecticut", "New England")
    df["State"] = df["State"].replace("New Hampshire", "New England")
    df["State"] = df["State"].replace("Massachusetts", "New England")
    df["State"] = df["State"].replace("New York", "Mid Atlantic")
    df["State"] = df["State"].replace("New York City", "Mid Atlantic")
    df["State"] = df["State"].replace("New Jersey", "Mid Atlantic")
    df["State"] = df["State"].replace("Pennsylvania", "Mid Atlantic")
    df["State"] = df["State"].replace("District of Columbia", "Mid Atlantic")
    df["State"] = df["State"].replace("Virginia", "Southern")
    df["State"] = df["State"].replace("West Virginia", "Southern")
    df["State"] = df["State"].replace("Kentucky", "Southern")
    df["State"] = df["State"].replace("Delaware", "Southern")
    df["State"] = df["State"].replace("Maryland", "Southern")
    df["State"] = df["State"].replace("North Carolina", "Southern")
    df["State"] = df["State"].replace("South Carolina", "Southern")
    df["State"] = df["State"].replace("Tennessee", "Southern")
    df["State"] = df["State"].replace("Arkansas", "Southern")
    df["State"] = df["State"].replace("Louisiana", "Southern")
    df["State"] = df["State"].replace("Florida", "Southern")
    df["State"] = df["State"].replace("Georgia", "Southern")
    df["State"] = df["State"].replace("Alabama", "Southern")
    df["State"] = df["State"].replace("Mississippi", "Southern")
    df["State"] = df["State"].replace("Michigan", "Mid West")
    df["State"] = df["State"].replace("North Dakota", "Mid West")
    df["State"] = df["State"].replace("South Dakota", "Mid West")
    df["State"] = df["State"].replace("Iowa", "Mid West")
    df["State"] = df["State"].replace("Minnesota", "Mid West")
    df["State"] = df["State"].replace("Kansas", "Mid West")
    df["State"] = df["State"].replace("Nebraska", "Mid West")
    df["State"] = df["State"].replace("Ohio", "Mid West")
    df["State"] = df["State"].replace("Indiana", "Mid West")
    df["State"] = df["State"].replace("Illinois", "Mid West")
    df["State"] = df["State"].replace("Wisconsin", "Mid West")
    df["State"] = df["State"].replace("Missouri", "Mid West")
    df["State"] = df["State"].replace("Texas", "South West")
    df["State"] = df["State"].replace("Arizona", "South West")
    df["State"] = df["State"].replace("New Mexico", "South West")
    df["State"] = df["State"].replace("Oklahoma", "South West")
    df["State"] = df["State"].replace("Montana", "Rocky Mountains")
    df["State"] = df["State"].replace("Idaho", "Rocky Mountains")
    df["State"] = df["State"].replace("Colorado", "Rocky Mountains")
    df["State"] = df["State"].replace("Utah", "Rocky Mountains")
    df["State"] = df["State"].replace("Wyoming", "Rocky Mountains")
    df["State"] = df["State"].replace("Nevada", "Rocky Mountains")
    df["State"] = df["State"].replace("California", "Pacific Coastal")
    df["State"] = df["State"].replace("Oregon", "Pacific Coastal")
    df["State"] = df["State"].replace("Washington", "Pacific Coastal")
    df["State"] = df["State"].replace("Alaska", "North West")
    df["State"] = df["State"].replace("Hawaii", "Oceanic")
    df["State"] = df["State"].replace("Puerto Rico", "Caribbean")
    df = df.rename({"State": "Region"}, axis=1)
    le_region = LabelEncoder()
    df["Region"] = le_region.fit_transform(df["Region"])
    le_sex = LabelEncoder()
    df["Sex"] = le_sex.fit_transform(df["Sex"])
    df["Deaths"] = [float(str(i).replace(",", "")) for i in df["Deaths"]]
    X = df.drop("Deaths", axis=1)
    y = df["Deaths"]
    y.iloc[y > 0] = 1
    np.random.seed(1)
    X_train,X_test,y_train, y_test = train_test_split(X,y,test_size=0.03,random_state= 1)
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train) 
    X_test = scaler.transform(X_test)
    logmodel_scaled = LogisticRegression(penalty='l2', solver='sag', max_iter=50)
    logmodel_scaled.fit(X_train,y_train)
    predictions_scaled = logmodel_scaled.predict(X_test)
    st.write(classification_report(y_test,predictions_scaled))
    st.subheader(f"The model accuracy is: {logmodel_scaled.score(X_test, y_test)}")


def show_explore_page():
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


    st.title("Modeling Summary: ")

    st.write("""
        ### Logistical Regression
    """)


    acc_butt = st.button("Show Model Accuracy Score")

    if acc_butt:
        data_clean()
        st.subheader("Model Breakdown: ")
        st.write("Ridge Regression: ")
        st.write("Code = LogisticRegression(penalty='l2', solver='sag', max_iter=50)")
        st.markdown("""
            The power of this Logistic Regression model accuracy comes from implementing the Ridge Regression penalty.
            This type of regularization prevents overfitting from occurring on the training dataset to ensure
            the testing dataset will perform to the best of its ability. The large variances between the training and testing
            data is how overfitting occurs. Ridge regression works by attempting to increase the bias or penalty 
            between the datasets. This increases the generalization between the two datasets, which creates a better fit. The additional penalty term equation
            added by using Ridge Regression on the model is: alpha * slope squared. This adjusts the slope based on a generalized 
            approach.
        """)
        st.image("https://i.stack.imgur.com/s71QZ.png", caption="Example of Ridge Regression.", width=250)
        
        

    # fig1, ax1 = plt.subplots()
    # ax1.pie(data, shadow=True, startangle=90)
    # ax1.axis("equal")
    # plt.legend(patches, bbox_to_anchor=(0,0.5), labels=data.index, loc="center left")
    # plt.tight_layout()

    
