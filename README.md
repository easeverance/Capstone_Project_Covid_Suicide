# Capstone_Project_Covid_Pandemic Predictor

## Hypothesis - Theory
Covid 19 has proven to be one of the worlds deadliest viral pandemics since the Spanish Flu in 1918.  This project is looking to see specifically in the US what could be causing more infections/deaths in specific locations in the US verus other locations in the US.  
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
  * Air Quality Statistics by County 2020  

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

* SciKitLearn 

### Dashboard

* Tableau
* GitHub
* SeaBorn

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






![lr_code](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/lr_model_code.PNG)


![model](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/Capture.PNG)

Above you can see a sample machine learning taking one variable to test against covid deaths. Here the variable English-Speaker shows that there is not a correlation to the the number of deaths.   Additional dependents will be added to the regression to get a better understanding of what factors can be used as predictors. 
