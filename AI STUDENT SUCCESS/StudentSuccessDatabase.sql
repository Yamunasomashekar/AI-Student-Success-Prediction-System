---creating database--
create database StudentSuccessDB;
use StudentSuccessDB;
CREATE TABLE StudentPredictions (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Hours_Studied FLOAT,
    Attendance FLOAT,
    Sleep_Hours FLOAT,
    Previous_Scores FLOAT,
    Tutoring_Sessions INT,
    Physical_Activity INT,
    Predicted_Score FLOAT,
    Recommendations VARCHAR(1000),
    Prediction_Date DATETIME DEFAULT GETDATE()
);

SELECT * 
FROM StudentPredictions;


ALTER TABLE StudentPredictions
ADD
    Parental_Involvement VARCHAR(20),
    Access_to_Resources VARCHAR(20),
    Extracurricular_Activities VARCHAR(10),
    Motivation_Level VARCHAR(20),
    Internet_Access VARCHAR(10),
    Family_Income VARCHAR(20),
    Teacher_Quality VARCHAR(20),
    School_Type VARCHAR(20),
    Peer_Influence VARCHAR(20),
    Learning_Disabilities VARCHAR(10),
    Parental_Education_Level VARCHAR(30),
    Distance_from_Home VARCHAR(20),
    Gender VARCHAR(10);