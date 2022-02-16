# Capstone_Project_Covid_Pandemic Predictor

## Hypothesis - Theory
Covid 19 has proven to be one of the worlds deadliest viral pandemics since the Spanish Flu in 1918.  This project is looking to see various geographical aspects and socio-economic aspects in US counties that could be causing more infections/deaths. US Counties could use this information for future outbreaks by addressing certain patterns that can be uncovered here.  

* What variables have a positive co-relation to Covid-19 infected areas. 
* Can we predict breakout areas and areas that are more vulnerable to future outbreaks

* H0 = that covid is an equal opportunity striker.  
* Ha = covid outbreaks can be predicted by specific socioeconomic markers.  Allowing one to predict future viral outbreaks.  

## Data Sources
* NY Times county level COVID19 case and fatality data
* USDA Economic Research Service
  * Unemploment and median household income for US, States, and counties 2000-20
  * Educational attainment for US, States, Counties 1970-2019
  * Population estimates for the US, States and Counties 2010 - 2020  
 

## Technology Used

### Data Cleaning and Analysis

* Python
* Jupyter Notebook
* Google Collab
* Matplotlib
* Pandas
* SASPy

### Database Storage

* pgAdmin
* PostgreSQL
* Heroku

![heroku_server](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/heroku_server.PNG)

### Machine Learning

* Unsupervised Machine Learning
* Supervised Machine Learning

### Dashboard

* Supervised Machine Learning
* Tableau (visualization)
* GitHub
* SeaBorn
<br></br>
* Unsupervised Machine Learning
* Streamlit (application)
* Pickle (binary encoding)
* Decision Tree Regression (ML)
* Pandas (bulk of data cleaning)

![dashboard](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/dashboard.PNG)

## Segment 1: Sketch It Out

The team is comprised of only Derek and Elizabeth - therefore there is no assigning square, triangle, circle or x responisbilities. 

### List of Deliverables for January 31st

* Topic for the project
* ReadMe
* Reposititory Management
* Identification of Technology
* Exploratory Data Analysis (ERD)
* Mockup of Machine Learning

### Exploratory Data Analysis (ERD)

![ERD](https://user-images.githubusercontent.com/90973718/152626094-d84711f8-23b6-4f57-95e3-cfc7b9b386a6.png)

### Database Storage

![Database Dashboard](https://user-images.githubusercontent.com/90973718/152647489-d2cd4ea1-304f-4d3d-a60f-a6dcc1b3c7f0.png)

![Database Query](https://user-images.githubusercontent.com/90973718/152647871-62ba2a85-ea33-4b65-9608-9291a922d70a.png)

### Database Schema

![create_table](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/dependents_table.PNG)

### Database Query

![dependents_table](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/dependents_data.PNG)


For our analysis  we will be using several datasets merged into one table 'Dependents'. This table includes variables such as employment, housing, income,  education, weather.  The second table will be on Covid deaths in the United States.  These two tables will be loaded into python where they will be merged into one DataFrame.  The data will further be cleaned and preprocessed and then set up for machine learning training.  
 
### Machine Learning

Early model building using cleaning table data.


![lr_code](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/lr_model_code.PNG)


![model](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/Capture.PNG)

Above you can see a sample machine learning taking one variable to test against covid deaths. Here the variable English-Speaker shows that there is not a correlation to the the number of deaths.  However, we are able to see that data needs to be cleaned more for specific FIPS areas in KSC and NYC.  These dependents caused outlier points.  Additional dependents will be added to the regression to get a better understanding of what factors can be used as predictors. 

# Segment Three: Build the Pieces

## Machine Learning Model

### Model Choice: Limitations and Benefits

For this project unsupervised machine learning was selected.  This was selected because we are looking for any groupings or trends with the selected data.   Unsupervised learning can be used in one of two ways: 1. Transform the data that can that be used for analysis or in another machine learning model, or 2. Clusters that assist in determing patterns in a grouping of data.   

Challenges: As with any machine learning, unsupervised machine learning poses it's own unique set of challenges.  Since unsupervised learning only looks at data as a whole - we can't be certain that the outcome that it is prediciting is correct. 

Benefits: Since we are not sure what variables if any has an effect this model allows us to visualize with graphs to explore the data. 

### Description of data preprocessing (Supervised)

Data sets were merged using pandas on the column "FIPS".  Next the data was cleaned using Pandas droping any NaN's, and unnecessary columns.  

![dataframe merge](https://user-images.githubusercontent.com/90973718/154164029-a53bfc5e-7921-4b1d-bb47-bf21f3ff65ac.png)

Next all of the unneccessary columns - datatype object were droped from the data set. 

![drop object  columns](https://user-images.githubusercontent.com/90973718/154164202-e626c16f-a554-49de-92fb-b9c55afe76b9.png)

All NaN's were dropped from the dataset. 

![drop nans](https://user-images.githubusercontent.com/90973718/154164631-80cc6d24-ef9a-4d79-b631-35e8b0af16ae.png)

Finally the data was scaled and normalized using Scikit-learn's StandardScale

![scale and normalize](https://user-images.githubusercontent.com/90973718/154165029-4bd086c2-afce-410c-9f96-f4def4e5551f.png)


<br>
</br>
### Description of data preprocessing (Unsupervised)



# Third Segment: Plug It In

## Machine Learning Model





