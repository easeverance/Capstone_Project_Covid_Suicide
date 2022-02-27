from matplotlib.pyplot import show
import streamlit as st
from app3_predict import show_predict_page
from app3_explore import show_explore_page
from app3_source import show_source_page

page = st.selectbox("Application Page Selection", ("Prediction Application", "Modeling Information", "Source Material"))

if page == "Prediction Application":
    show_predict_page()
elif page == "Source Material":
    show_source_page()
else:
    show_explore_page()
