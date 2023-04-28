# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
The goal of this project was to create a model to predict whether a person would be approved for a loan or not and to deploy that model to the cloud.

&nbsp;
## Hypothesis
Features such as credit history, applicant income and loan amount are correlated with whether or not a person is more or less likely to be approved for a loan.

&nbsp;
## EDA 
* Credit history seems to be the best indicator for whether a person gets approved for a loan or not
    * A person with a credit history is much more likely to be approved for a loan (~80% approval rate) than a person without (~8% approval rate).
* Other factors that seem to play a discernable role in wheter a person is approved or not include: Education level, Property Area and Marital status
* Whether or not a person was self employed did not seem to factor in to whether or not the person was approved for a loan



&nbsp;
## Process
* EDA 
    * Checking for nulls
    * Distribution analysis
    * Comparison of numerical and categorical variables
    * Visualisations --> Barplots, Histograms, kdeplot, boxplots etc.
* Data Cleaning and Feature Engineering
    * Impute missing values 
    * Created new features ('Total Income')
    * Data Transformation
    * Select features for model
* Modeling
    * Random Forest Classifier
    * Hyperparameter tuning
    * Deployment and testing

Note: This was not a fully linear process.

&nbsp;
## Results/Demo
The final model selected was a Random Forest Classifier. After tuning, the final model had an accuracy score of 0.82 and a f1 score of 0.76.

&nbsp;
## Challenges 
* The biggest challenge for this project was definitely the time constraint since it was only a one day project. I felt I was rushing through many parts just to get the project completed in time and there were things that I would have liked to do but did not get around to doing because of the time constraint.
* Gridsearch was really putting a strain on my PC and I had to cut down on the number of hyperparameter inputs to test when running it.

&nbsp;
## Future Goals
* Test a greater number of models
* Do more feature engineering and implement a more robust feature selection process.


&nbsp;
### Note: For a more detailed walkthrough of the EDA, Process and Results of this project, please refer to the 'instructions.ipnyb' notebook located in the 'notebook' folder. 