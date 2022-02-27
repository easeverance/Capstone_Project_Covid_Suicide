import streamlit as st

def show_source_page():
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

    st.title("Source Material")
    st.write("Covid-19 Deaths in the US - Kaggle Dataset - Edward Zhang")
    url = "https://www.kaggle.com/sshikamaru/covid19-deaths-in-the-us"
    st.write("Check out this [dataset](%s)" % url)
    st.write()
    st.write("Build a Lookalike Logistic Regression Model with SKLearn and Keras - Ridge Regression - Firas Obeid")
    url_2 = "https://medium.com/analytics-vidhya/build-lookalike-logistic-regression-model-with-sklearn-and-keras-2b03c540cdd5"
    st.write("Check out this [article](%s)" % url_2)

    

    