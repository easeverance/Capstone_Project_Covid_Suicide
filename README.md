# Capstone_Project_Covid_Pandemic Predictor

## Hypothesis - Theory
Covid 19 has proven to be one of the worlds deadliest viral pandemics since the Spanish Flu in 1918.  This project is looking to see various geographical aspects and socio-economic aspects in US counties that could be causing more infections/deaths. US Counties could use this information for future outbreaks by addressing certain patterns that can be uncovered here.  

* What variables have a positive co-relation to Covid-19 infected areas. 
* Can we predict breakout areas and areas that are more vulnerable to future outbreaks

* H0 = that covid is an equal opportunity striker.  
* Ha = covid outbreaks can be predicted by specific socioeconomic markers.  Allowing one to predict future viral outbreaks.  

### Google Slides Presentation
[Presentation Link](https://docs.google.com/presentation/d/1llWIpjVPxFYgyfi3QGZCrpzqbH43CRMLmmlway6LdCc/edit?usp=sharing)

## Data Sources
* NY Times county level COVID19 case and fatality data
  * [Dataset Link](https://github.com/nytimes/covid-19-data)
* USDA Economic Research Service
  * Unemploment and median household income for US, States, and counties 2000-20
   * [Dataset Link](https://www.ers.usda.gov/webdocs/DataFiles/48747/Unemployment.xls)
  * Educational attainment for US, States, Counties 1970-2019
  * [Dataset Link](https://www.ers.usda.gov/webdocs/DataFiles/48747/Education.xls)
  * Population estimates for the US, States and Counties 2010 - 2020
  * [Dataset Link](https://www.census.gov/programs-surveys/popest/technical-documentation/research/evaluation-estimates/2020-evaluation-estimates/2010s-counties-total.html)  
* Covid-19 Deaths in the US Dataset - Edward Zhang
  * [Dataset Link](https://www.kaggle.com/sshikamaru/covid19-deaths-in-the-us)

### Cleaned Data
* appdata_clean.ipynb - Jupyter Notebook Cleaning Pipeline (Resources)
* covid19.csv - Cleaned Data for Prediction Dashboard (Resources)
 

## Technology Used

### Data Cleaning and Analysis

* Python
* Jupyter Notebook
* Google Collab
* Matplotlib
* Seaborn
* Pandas
* Numpy
* SASPy
* Sci-kit Learn
* Pickle
* Scipy

### Database Storage

* pgAdmin
* PostgreSQL
* Heroku




## Segment 1: Sketch It Out

The team is comprised of only Derek and Elizabeth - therefore there is no assigning square, triangle, circle or x responisbilities. 

### List of Deliverables for January 31st

* Topic for the project
* ReadMe
* Reposititory Management
* Identification of Technology
* Exploratory Data Analysis (ERD)
* Mockup of Machine Learning



## Database Structure

### Exploratory Data Analysis (ERD)

![ERD](https://user-images.githubusercontent.com/90973718/152626094-d84711f8-23b6-4f57-95e3-cfc7b9b386a6.png)

### Database Storage

![Database Dashboard](https://user-images.githubusercontent.com/90973718/152647489-d2cd4ea1-304f-4d3d-a60f-a6dcc1b3c7f0.png)

![Database Query](https://user-images.githubusercontent.com/90973718/152647871-62ba2a85-ea33-4b65-9608-9291a922d70a.png)

### Database Server-side

![heroku_server](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/heroku_server.PNG)

### Database Schema

![create_table](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/dependents_table.PNG)

### Database Query

![dependents_table](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/dependents_data.PNG)


For our analysis  we will be using several datasets merged into one table 'Dependents'. This table includes variables such as employment, housing, income,  education, weather.  The second table will be on Covid deaths in the United States.  These two tables will be loaded into python where they will be merged into one DataFrame.  The data will further be cleaned and preprocessed and then set up for machine learning training.  
 

Above you can see a sample machine learning taking one variable to test against covid deaths. Here the variable English-Speaker shows that there is not a correlation to the the number of deaths.  However, we are able to see that data needs to be cleaned more for specific FIPS areas in KSC and NYC.  These dependents caused outlier points.  Additional dependents will be added to the regression to get a better understanding of what factors can be used as predictors. 

# Segment Three: Build the Pieces

## Machine Learning Selection (In-Depth)

### Model Choice: Limitations and Benefits

For this project unsupervised machine learning was selected.  This was selected because we are looking for any groupings or trends with the selected data.   Unsupervised learning can be used in one of two ways: 1. Transform the data that can that be used for analysis or in another machine learning model, or 2. Clusters that assist in determing patterns in a grouping of data.   

Challenges: As with any machine learning, unsupervised machine learning poses it's own unique set of challenges.  Since unsupervised learning only looks at data as a whole - we can't be certain that the outcome that it is prediciting is correct. 

Benefits: Since we are not sure what variables if any has an effect this model allows us to visualize with graphs to explore the data. 

## Description of data preprocessing (Unsupervised)

Data sets were merged using pandas on the column "FIPS".  Next the data was cleaned using Pandas droping any NaN's, and unnecessary columns.  

![dataframe merge](https://user-images.githubusercontent.com/90973718/154164029-a53bfc5e-7921-4b1d-bb47-bf21f3ff65ac.png)

Next all of the unneccessary columns - datatype object were droped from the data set. 

![drop object  columns](https://user-images.githubusercontent.com/90973718/154164202-e626c16f-a554-49de-92fb-b9c55afe76b9.png)

All NaN's were dropped from the dataset. 

![drop nans](https://user-images.githubusercontent.com/90973718/154164631-80cc6d24-ef9a-4d79-b631-35e8b0af16ae.png)

Finally the data was scaled and normalized using Scikit-learn's StandardScale

![scale and normalize](https://user-images.githubusercontent.com/90973718/154165029-4bd086c2-afce-410c-9f96-f4def4e5551f.png)



## Description of data preprocessing (Supervised)

The data set was cleaned by removing all columns except the necessary features and independent values.
Column information was also renamed for better readability.
Exploratory cleaning was also done by searching and removing all null data.

![unclean1](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/unclean1.PNG)

The data was then checked to ensure the null values were purged. 
Also, the unnecessary rows were dropped, such as those grouped by year instead of by month.

![unclean2](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/unclean2.PNG)

Functions were applied to the necessary features to create a float array.
This will be necessary for the binary encoding transformation.

![unfunc1](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/unfunc1.PNG)

The state series was grouped into regional bins to provide more exploratory predictions for the app.

![ungroup1](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/ungroup1.PNG)

The region and sex columns were fit to the encoders for binary categorizing. 

![unencode1](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/unencode1.PNG)

The commas were removed from the independent deaths data before transforming to float values.
The X features and y independent values were assigned.
A linear regression model was then created and the values were fit.

![unlinreg1](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/unlinreg1.PNG)

Using the mean squared error module to find the difference between the actual deaths and predicted deaths.
This error calculation was used for all machine learning models to test the accuracy against the data.

![unlinreg2](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/unlinreg2.PNG)

A Decision Tree Regressor was fit and predicted against the values, which had improved accuracy versus the Linear Regression model.

![undectree1](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/undectree1.PNG)

A Random Forest Regressor was also created, fit and predicted, which had similar accuracy to the Decision Tree.

![unranfor1](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/unranfor1.PNG)

A fit and score method of the GridSearchCV module was used on the Decision Tree Regressor.
Multiple max_depth parameters were created to test and score.
Mean Squared Error scoring was used to find the mean squared errors of each parameter.
The GridSearchCV was then fit to the values.

The Best Estimator module of GridSearchCV was used to fit the values.
Then added the predict module to the features.
The y and y_pred values were passed using the Mean Squared Error module.

![gridsearch1](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/gridsearch1.PNG)

A template array was creating to use in the application. These values will be replaced using the feature selectors.

![modelarray1](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/modelarray1.PNG)

The regressor model was then saved in the Pickle data file that can be opened in the prediction application.

![pickle1](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/pickle1.PNG)


# Third Segment: Plug It In

During the 3rd Segment of the capstone project we are adding the final touches and plugging the data into our models to see where we are at. 

## Machine Learning

### Supervised Machine Learning
Creating the Logistic Regression model and scaler. Fitting, Predicting, and the creation of test and train sets take place.
![lr_modelpic](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/lr_model_pic.PNG)
<br></br>
Creating the Ridge Regression Penalty to help Generalize the model (train vs test) for better accuracy.
![l2_ridge](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/l2_ridge.PNG)



## Dashboard

### Supervised Machine Learning
* Streamlit (application)
* GitHub
* Pickle (binary encoding)
* Logistic Regression (ML)
* Ridge Regression Generalization
* Pandas (bulk of data cleaning)

[Dashboard Link](https://covidappproject.herokuapp.com/)

![dashboard](https://github.com/easeverance/Capstone_Project_Covid_Suicide/blob/main/markdownpics/dash_b.PNG)

## Summary & Conclusion

The results of the machine learning confirmed most of what we have already learned about the covid pandemic: people who live in more populated areas, have limited English, live in multi-unit housing, lower income levels are more inclined die from covid and be affected from future outbreaks. Those who live in less populated areas and have obtained higher education are less likely to affected by the virus or future pandemics. 

![heatmap supervised learning](https://user-images.githubusercontent.com/90973718/156273224-65104f85-ca1d-4815-9525-1b5baf346b54.png)







