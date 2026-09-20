# AI-Powered Student Success Prediction & Recommendation System

## 📌 Project Overview

The **AI-Powered Student Success Prediction & Recommendation System** is a machine learning-based web application designed to predict a student's examination score based on academic, personal, and learning-related factors.

The system also provides personalized recommendations based on the student's input values to help identify areas that may need improvement.

The application uses a machine learning model for prediction, Flask for the backend, HTML/CSS/JavaScript for the frontend, and SQL Server for storing prediction history.

---

## 🎯 Objectives

- Predict a student's examination score using machine learning.
- Analyze important factors affecting student performance.
- Provide personalized recommendations to students.
- Store prediction results in a database.
- Provide a prediction history page.
- Provide a dashboard for analyzing prediction results.
- Develop a complete machine learning web application.

---

## 🚀 Features

- Student performance prediction
- Machine learning-based score prediction
- Personalized recommendations
- Input validation
- Prediction history
- Search prediction history
- Dashboard with statistics
- Score category classification
- SQL Server database integration
- Flask web application
- Responsive user interface

---

# 🛠️ Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

### Data Analysis

- Pandas
- NumPy
- Matplotlib

### Backend

- Flask

### Frontend

- HTML
- CSS
- JavaScript

### Database

- Microsoft SQL Server
- PyODBC

### Development Tools

- Visual Studio Code
- Jupyter Notebook
- SQL Server Management Studio

---

# 📊 Dataset

The project uses the **Student Performance Factors** dataset.

The dataset contains **6,607 student records** and **20 original columns**.

## Main Features

- Hours Studied
- Attendance
- Parental Involvement
- Access to Resources
- Extracurricular Activities
- Sleep Hours
- Previous Scores
- Motivation Level
- Internet Access
- Tutoring Sessions
- Family Income
- Teacher Quality
- School Type
- Peer Influence
- Physical Activity
- Learning Disabilities
- Parental Education Level
- Distance from Home
- Gender
- Exam Score

## Target Variable

```text
Exam_Score
```

---

# 🔄 Project Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Data Transformation
   ↓
Missing Value Handling
   ↓
Duplicate Checking
   ↓
Categorical Encoding
   ↓
Exploratory Data Analysis
   ↓
Correlation Analysis
   ↓
Data Visualization
   ↓
Target Separation
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Selection
   ↓
Save Best Model
   ↓
Recommendation System
   ↓
Flask Backend
   ↓
SQL Server
   ↓
Frontend
   ↓
Prediction
   ↓
History & Dashboard
```

---

# 🧹 1. Data Cleaning

Data cleaning was performed before training the machine learning models.

## 1.1 Checking Dataset Information

The dataset was inspected using:

```python
df.info()
```

This was used to understand:

- Number of rows
- Number of columns
- Data types
- Missing values

---

## 1.2 Checking Dataset Shape

```python
df.shape
```

The original dataset contained:

```text
6607 rows
20 columns
```

---

## 1.3 Checking Missing Values

Missing values were identified using:

```python
df.isnull().sum()
```

Missing values were found in:

| Column | Missing Values |
|---|---:|
| Teacher_Quality | 78 |
| Parental_Education_Level | 90 |
| Distance_from_Home | 67 |

Total missing values:

```text
235
```

---

## 1.4 Handling Missing Values

Missing categorical values were handled using the mode of each column.

```python
for col in [
    "Teacher_Quality",
    "Parental_Education_Level",
    "Distance_from_Home"
]:
    df[col] = df[col].fillna(df[col].mode()[0])
```

After this step, the missing values were handled.

---

## 1.5 Checking Duplicate Records

Duplicate records were checked using:

```python
df.duplicated().sum()
```

The dataset contained:

```text
0 duplicate records
```

Therefore, no duplicate rows needed to be removed.

---

# 🔢 2. Data Transformation

The dataset contained both numerical and categorical variables.

Machine learning models require numerical input, so categorical variables were converted into numerical representation.

## 2.1 One-Hot Encoding

One-hot encoding was performed using:

```python
df = pd.get_dummies(
    df,
    drop_first=True,
    dtype=int
)
```

### Why One-Hot Encoding?

Categorical values such as:

```text
Low
Medium
High
```

cannot be directly used by the machine learning model.

They were converted into numerical columns.

For example:

```text
Parental_Involvement
```

was transformed into columns such as:

```text
Parental_Involvement_Low
Parental_Involvement_Medium
```

The reference category was represented by zeros because:

```python
drop_first=True
```

was used.

---

## 2.2 Final Dataset Shape

After preprocessing and encoding:

```text
Rows: 6607
Columns: 28
```

There were:

```text
27 input features
1 target variable
```

---

# 📈 3. Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand the dataset before model training.

The following analysis was performed:

- Statistical analysis
- Correlation analysis
- Histograms
- Scatter plots
- Correlation heatmap
- Bar charts

---

## 3.1 Statistical Analysis

Statistical information was obtained using:

```python
df.describe()
```

This was used to examine:

- Mean
- Standard deviation
- Minimum
- Maximum
- 25th percentile
- 50th percentile
- 75th percentile

for numerical variables.

---

## 3.2 Correlation Analysis

Correlation analysis was performed to understand the relationship between numerical variables and examination score.

```python
df.corr()
```

Important correlations with `Exam_Score` observed in the dataset included:

| Feature | Approximate Correlation |
|---|---:|
| Attendance | 0.581 |
| Hours_Studied | 0.446 |
| Previous_Scores | 0.175 |
| Tutoring_Sessions | 0.156 |

These values describe relationships observed in this dataset.

---

## 3.3 Histogram

Histograms were created to understand the distribution of numerical variables.

Histograms helped visualize:

- Distribution of values
- Concentration of observations
- Spread of numerical variables
- Possible unusual values

---

## 3.4 Scatter Plot

Scatter plots were used to visualize relationships between important numerical variables and examination score.

Examples include:

```text
Hours_Studied vs Exam_Score
Attendance vs Exam_Score
Previous_Scores vs Exam_Score
```

These visualizations helped understand how changes in numerical variables were associated with examination scores.

---

## 3.5 Correlation Heatmap

A correlation heatmap was created to visualize relationships between numerical features.

The heatmap helped identify:

- Positive correlations
- Negative correlations
- Weak relationships
- Stronger relationships

---

## 3.6 Bar Chart

Bar charts were used to visualize and compare values across relevant categories.

This helped understand differences between categorical groups.

---

# 🎯 4. Target Separation

The target variable was separated from the input features.

```python
X = df.drop("Exam_Score", axis=1)
y = df["Exam_Score"]
```

Where:

```text
X = Input Features
y = Target Variable
```

The resulting shapes were:

```text
X = (6607, 27)
y = (6607,)
```

### Important

This step separates the target from the input variables.

It does not mean that irrelevant features were removed.

---

# ✂️ 5. Train-Test Split

The dataset was divided into training and testing data.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

The dataset was divided into:

```text
Training records: 5285
Testing records: 1322
```

The training data was used to train the models.

The testing data was used to evaluate model performance.

---

# 🤖 6. Machine Learning Model Training

Three regression models were trained.

## 6.1 Linear Regression

Linear Regression was trained to predict the examination score.

It was used as a regression model to establish the relationship between input features and the target score.

---

## 6.2 Decision Tree Regressor

A Decision Tree Regressor was trained to predict examination scores.

The model uses decision rules based on input features to make predictions.

---

## 6.3 Random Forest Regressor

A Random Forest Regressor was trained using multiple decision trees.

The predictions from the trees are combined to produce the final prediction.

---

# 📏 7. Model Evaluation

The models were evaluated using three metrics.

## Mean Absolute Error (MAE)

Measures the average absolute difference between actual and predicted values.

## Root Mean Squared Error (RMSE)

Measures prediction error while giving greater weight to larger errors.

## R² Score

Measures how much variation in the target variable is explained by the model.

---

# 📊 8. Model Comparison

The actual evaluation results obtained from the project were:

| Model | MAE | RMSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 0.45 | 1.80 | 0.770 |
| Decision Tree | 1.88 | 3.75 | 0.006 |
| Random Forest | 1.18 | 2.23 | 0.649 |

Based on these evaluation results, Linear Regression was selected for the application.

---

# 💾 9. Model Saving

The trained Linear Regression model was saved using Pickle.

```python
import pickle

with open("linear_regression_model.pkl", "wb") as file:
    pickle.dump(lr_model, file)
```

The saved model file is:

```text
linear_regression_model.pkl
```

The Flask application loads this saved model to generate predictions.

---

# 💡 10. Recommendation System

A recommendation system was developed to provide personalized suggestions based on student inputs.

The recommendation system is implemented in:

```text
recommendation.py
```

Recommendations can include:

- Increasing study hours
- Improving attendance
- Considering additional tutoring
- Improving sleep habits
- Strengthening basic concepts
- Improving motivation
- Making better use of learning resources
- Using offline study materials
- Including physical activity
- Seeking additional academic support

The recommendation system checks the student's submitted values and generates relevant suggestions.

---

# 🌐 11. Flask Web Application

Flask was used to develop the backend of the web application.

The main backend file is:

```text
app.py
```

The application performs the following tasks:

```text
Receive Student Input
        ↓
Validate Input
        ↓
Prepare Model Features
        ↓
Load Saved Model
        ↓
Generate Prediction
        ↓
Generate Recommendations
        ↓
Store Result in SQL Server
        ↓
Display Result
```

---

# 📝 12. Student Input

The application accepts 19 student-related inputs.

These include:

1. Hours Studied
2. Attendance
3. Parental Involvement
4. Access to Resources
5. Extracurricular Activities
6. Sleep Hours
7. Previous Scores
8. Motivation Level
9. Internet Access
10. Tutoring Sessions
11. Family Income
12. Teacher Quality
13. School Type
14. Peer Influence
15. Physical Activity
16. Learning Disabilities
17. Parental Education Level
18. Distance from Home
19. Gender

---

# 🔐 13. Input Validation

Input validation was implemented to prevent invalid values from being processed.

Examples of validation include:

| Input | Valid Range / Values |
|---|---|
| Hours Studied | 1–44 |
| Attendance | 60–100 |
| Sleep Hours | 4–10 |
| Previous Scores | 50–100 |
| Tutoring Sessions | 0–8 |
| Physical Activity | 0–6 |

Categorical fields are also validated against their allowed values.

Invalid inputs are rejected and are not stored in the database.

---

# 🎯 14. Prediction

After successful validation, the student's inputs are converted into the feature format expected by the trained model.

The saved Linear Regression model then generates the predicted examination score.

The prediction is displayed on the result page.

---

# 🏷️ 15. Performance Categories

The predicted score is classified into four categories:

| Score | Category |
|---|---|
| 90 and above | Excellent |
| 75–89.99 | Good |
| 60–74.99 | Average |
| Below 60 | Needs Improvement |

These categories are used in the result page and dashboard.

---

# 🗄️ 16. SQL Server Database

Microsoft SQL Server is used to store prediction information.

## Database

```text
StudentSuccessDB
```

## Table

```text
StudentPredictions
```

The table stores:

- Student input values
- Predicted score
- Recommendations
- Prediction date
- Prediction ID

The SQL database setup is stored in:

```text
StudentSuccessDatabase.sql
```

---

# 📜 17. Prediction History

The application provides a prediction history page.

The history page displays previously stored predictions.

It includes information such as:

- Prediction ID
- Hours Studied
- Attendance
- Sleep Hours
- Previous Scores
- Tutoring Sessions
- Physical Activity
- Predicted Score
- Recommendations
- Prediction Date

The history page also provides search functionality.

Examples:

```text
ID 1
score 76.05
hours 40
attendance 87
```

---

# 📊 18. Dashboard

A dashboard was developed to provide an overview of prediction results.

## KPI Statistics

- Total Predictions
- Average Predicted Score
- Highest Predicted Score
- Lowest Predicted Score

## Performance Categories

- Excellent
- Good
- Average
- Needs Improvement

## Visualizations

- Predicted Score Bar Chart
- Performance Category Doughnut Chart

The dashboard obtains prediction information from the SQL Server database.

---

# 🖥️ 19. Frontend Pages

The application contains the following HTML pages:

```text
templates/
│
├── index.html
├── result.html
├── history.html
└── dashboard.html
```

### index.html

Student input form.

### result.html

Displays:

- Predicted score
- Performance category
- Personalized recommendations

### history.html

Displays stored prediction records and search functionality.

### dashboard.html

Displays prediction statistics and charts.

---

# 📁 20. Project Structure

```text
AI STUDENT SUCCESS
│
├── Dataset/
│   └── StudentPerformanceFactors.csv
│
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── history.html
│   └── dashboard.html
│
├── app.py
├── recommendation.py
├── recommendation.ipynb
├── model_training_dataset.ipynb
├── cleaned_training_student_dataset.csv
├── linear_regression_model.pkl
├── test_sql.py
├── StudentSuccessDatabase.sql
├── requirements.txt
└── README.md
```

---

# 🛠️ 21. Technologies Used

## Programming Language

```text
Python
```

## Data Analysis

```text
Pandas
NumPy
Matplotlib
```

## Machine Learning

```text
Scikit-learn
```

## Machine Learning Models

```text
Linear Regression
Decision Tree Regressor
Random Forest Regressor
```

## Backend

```text
Flask
```

## Frontend

```text
HTML
CSS
JavaScript
```

## Database

```text
Microsoft SQL Server
PyODBC
```

## Development Tools

```text
Visual Studio Code
Jupyter Notebook
SQL Server Management Studio
```

---

# ▶️ 22. How to Run the Project

## Step 1: Install Dependencies

Open the terminal in the project folder.

Run:

```bash
pip install -r requirements.txt
```

---

## Step 2: Configure SQL Server

Open:

```text
StudentSuccessDatabase.sql
```

Create the database and table in SQL Server Management Studio.

The database is:

```text
StudentSuccessDB
```

---

## Step 3: Start Flask

Open the terminal in VS Code and run:

```bash
python app.py
```

---

## Step 4: Open the Application

Open:

```text
http://127.0.0.1:5000
```

in a web browser.

---

# 🔄 23. Complete Application Workflow

```text
                    STUDENT
                       │
                       ↓
                Frontend Form
                       │
                       ↓
                Flask Backend
                       │
                       ↓
                Input Validation
                       │
                       ↓
             Feature Transformation
                       │
                       ↓
             Saved ML Model (.pkl)
                       │
                       ↓
              Predicted Exam Score
                       │
                       ↓
             Recommendation System
                       │
              ┌────────┴────────┐
              ↓                 ↓
         SQL Server         Result Page
              │                 │
              ↓                 ↓
      Prediction History     Score
              │              Category
              ↓           Recommendations
         Dashboard
```

---

# 📌 24. Current Project Status

The following components have been implemented:

- [x] Dataset collection
- [x] Data cleaning
- [x] Missing value handling
- [x] Duplicate checking
- [x] Categorical encoding
- [x] Exploratory Data Analysis
- [x] Correlation analysis
- [x] Data visualization
- [x] Target separation
- [x] Train-test split
- [x] Machine learning model training
- [x] Model evaluation
- [x] Model selection
- [x] Model saving
- [x] Recommendation system
- [x] Flask backend
- [x] Frontend
- [x] Input validation
- [x] SQL Server integration
- [x] Prediction history
- [x] Search functionality
- [x] Dashboard
- [x] Charts and visualizations

---

# 🔮 25. Future Enhancements

Possible future improvements include:

- Student login and authentication
- Individual student profiles
- Cloud deployment
- Advanced recommendation techniques
- Additional machine learning models
- Automatic model retraining
- Long-term student performance tracking
- More advanced dashboard analytics
- Mobile-friendly application
- Notification system

---

# 👩‍💻 Project

## AI-Powered Student Success Prediction & Recommendation System

A machine learning-based web application for predicting student examination performance and providing personalized academic recommendations.