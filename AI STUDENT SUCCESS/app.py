from flask import Flask, render_template, request
import pickle
import pyodbc
import pandas as pd
from recommendation import get_recommendations


# =========================================================
# FLASK APP
# =========================================================

app = Flask(__name__)


# =========================================================
# LOAD TRAINED MODEL
# =========================================================

with open("linear_regression_model.pkl", "rb") as file:
    model = pickle.load(file)

print("Linear Regression model loaded successfully!")


# =========================================================
# SQL SERVER CONNECTION
# =========================================================

def get_connection():

    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=StudentSuccessDB;"
        "Trusted_Connection=yes;"
    )

    return connection


# =========================================================
# SAVE PREDICTION TO SQL SERVER
# =========================================================

def save_prediction(
    hours,
    attendance,
    parental_involvement,
    resources,
    extracurricular,
    sleep,
    previous_scores,
    motivation,
    internet,
    tutoring,
    income,
    teacher,
    school,
    peer,
    physical_activity,
    disability,
    education,
    distance,
    gender,
    prediction,
    recommendations
):

    connection = get_connection()

    cursor = connection.cursor()

    recommendations_text = "; ".join(recommendations)


    cursor.execute("""
        INSERT INTO StudentPredictions
        (
            Hours_Studied,
            Attendance,
            Sleep_Hours,
            Previous_Scores,
            Tutoring_Sessions,
            Physical_Activity,
            Parental_Involvement,
            Access_to_Resources,
            Extracurricular_Activities,
            Motivation_Level,
            Internet_Access,
            Family_Income,
            Teacher_Quality,
            School_Type,
            Peer_Influence,
            Learning_Disabilities,
            Parental_Education_Level,
            Distance_from_Home,
            Gender,
            Predicted_Score,
            Recommendations
        )

        VALUES
        (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
    """,

        hours,
        attendance,
        sleep,
        previous_scores,
        tutoring,
        physical_activity,

        parental_involvement,
        resources,
        extracurricular,
        motivation,
        internet,
        income,
        teacher,
        school,
        peer,
        disability,
        education,
        distance,
        gender,

        prediction,
        recommendations_text
    )


    connection.commit()

    cursor.close()

    connection.close()


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/")
def home():

    return render_template("index.html")


# =========================================================
# PREDICTION
# =========================================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # =================================================
        # GET FORM VALUES
        # =================================================

        hours = request.form.get("Hours_Studied", "").strip()
        attendance = request.form.get("Attendance", "").strip()

        parental_involvement = request.form.get(
            "Parental_Involvement", ""
        ).strip()

        resources = request.form.get(
            "Access_to_Resources", ""
        ).strip()

        extracurricular = request.form.get(
            "Extracurricular_Activities", ""
        ).strip()

        sleep = request.form.get(
            "Sleep_Hours", ""
        ).strip()

        previous_scores = request.form.get(
            "Previous_Scores", ""
        ).strip()

        motivation = request.form.get(
            "Motivation_Level", ""
        ).strip()

        internet = request.form.get(
            "Internet_Access", ""
        ).strip()

        tutoring = request.form.get(
            "Tutoring_Sessions", ""
        ).strip()

        income = request.form.get(
            "Family_Income", ""
        ).strip()

        teacher = request.form.get(
            "Teacher_Quality", ""
        ).strip()

        school = request.form.get(
            "School_Type", ""
        ).strip()

        peer = request.form.get(
            "Peer_Influence", ""
        ).strip()

        physical_activity = request.form.get(
            "Physical_Activity", ""
        ).strip()

        disability = request.form.get(
            "Learning_Disabilities", ""
        ).strip()

        education = request.form.get(
            "Parental_Education_Level", ""
        ).strip()

        distance = request.form.get(
            "Distance_from_Home", ""
        ).strip()

        gender = request.form.get(
            "Gender", ""
        ).strip()


        # =================================================
        # NUMERIC VALIDATION
        # =================================================

        try:

            hours = float(hours)
            attendance = float(attendance)
            sleep = float(sleep)
            previous_scores = float(previous_scores)
            tutoring = int(tutoring)
            physical_activity = int(physical_activity)

        except ValueError:

            return render_template(
                "index.html",
                validation_error="Please enter valid numeric values."
            )


        # =================================================
        # RANGE VALIDATION
        # =================================================

        if not 1 <= hours <= 44:

            return render_template(
                "index.html",
                validation_error=
                "Invalid Hours Studied. Enter a value between 1 and 44."
            )


        if not 60 <= attendance <= 100:

            return render_template(
                "index.html",
                validation_error=
                "Invalid Attendance. Enter a value between 60 and 100."
            )


        if not 4 <= sleep <= 10:

            return render_template(
                "index.html",
                validation_error=
                "Invalid Sleep Hours. Enter a value between 4 and 10."
            )


        if not 50 <= previous_scores <= 100:

            return render_template(
                "index.html",
                validation_error=
                "Invalid Previous Scores. Enter a value between 50 and 100."
            )


        if not 0 <= tutoring <= 8:

            return render_template(
                "index.html",
                validation_error=
                "Invalid Tutoring Sessions. Enter a value between 0 and 8."
            )


        if not 0 <= physical_activity <= 6:

            return render_template(
                "index.html",
                validation_error=
                "Invalid Physical Activity. Enter a value between 0 and 6."
            )


        # =================================================
        # CATEGORICAL VALIDATION
        # =================================================

        if parental_involvement not in [
            "Low",
            "Medium",
            "High"
        ]:

            return render_template(
                "index.html",
                validation_error=
                "Invalid Parental Involvement."
            )


        if resources not in [
            "Low",
            "Medium",
            "High"
        ]:

            return render_template(
                "index.html",
                validation_error=
                "Invalid Access to Resources."
            )


        if extracurricular not in [
            "Yes",
            "No"
        ]:

            return render_template(
                "index.html",
                validation_error=
                "Invalid Extracurricular Activities value."
            )


        if motivation not in [
            "Low",
            "Medium",
            "High"
        ]:

            return render_template(
                "index.html",
                validation_error=
                "Invalid Motivation Level."
            )


        if internet not in [
            "Yes",
            "No"
        ]:

            return render_template(
                "index.html",
                validation_error=
                "Invalid Internet Access value."
            )


        if income not in [
            "Low",
            "Medium",
            "High"
        ]:

            return render_template(
                "index.html",
                validation_error=
                "Invalid Family Income."
            )


        if teacher not in [
            "Low",
            "Medium",
            "High"
        ]:

            return render_template(
                "index.html",
                validation_error=
                "Invalid Teacher Quality."
            )


        if school not in [
            "Public",
            "Private"
        ]:

            return render_template(
                "index.html",
                validation_error=
                "Invalid School Type."
            )


        if peer not in [
            "Positive",
            "Neutral",
            "Negative"
        ]:

            return render_template(
                "index.html",
                validation_error=
                "Invalid Peer Influence."
            )


        if disability not in [
            "Yes",
            "No"
        ]:

            return render_template(
                "index.html",
                validation_error=
                "Invalid Learning Disabilities value."
            )


        if education not in [
            "High School",
            "College",
            "Postgraduate"
        ]:

            return render_template(
                "index.html",
                validation_error=
                "Invalid Parental Education Level."
            )


        if distance not in [
            "Near",
            "Moderate",
            "Far"
        ]:

            return render_template(
                "index.html",
                validation_error=
                "Invalid Distance from Home."
            )


        if gender not in [
            "Male",
            "Female"
        ]:

            return render_template(
                "index.html",
                validation_error=
                "Invalid Gender."
            )


        # =================================================
        # CREATE MODEL INPUT
        # =================================================

        model_columns = [

            "Hours_Studied",
            "Attendance",
            "Sleep_Hours",
            "Previous_Scores",
            "Tutoring_Sessions",
            "Physical_Activity",

            "Parental_Involvement_Low",
            "Parental_Involvement_Medium",

            "Access_to_Resources_Low",
            "Access_to_Resources_Medium",

            "Extracurricular_Activities_Yes",

            "Motivation_Level_Low",
            "Motivation_Level_Medium",

            "Internet_Access_Yes",

            "Family_Income_Low",
            "Family_Income_Medium",

            "Teacher_Quality_Low",
            "Teacher_Quality_Medium",

            "School_Type_Public",

            "Peer_Influence_Neutral",
            "Peer_Influence_Positive",

            "Learning_Disabilities_Yes",

            "Parental_Education_Level_High School",
            "Parental_Education_Level_Postgraduate",

            "Distance_from_Home_Moderate",
            "Distance_from_Home_Near",

            "Gender_Male"
        ]


        # Start all features with zero

        input_data = {
            column: 0
            for column in model_columns
        }


        # Numerical features

        input_data["Hours_Studied"] = hours

        input_data["Attendance"] = attendance

        input_data["Sleep_Hours"] = sleep

        input_data["Previous_Scores"] = previous_scores

        input_data["Tutoring_Sessions"] = tutoring

        input_data["Physical_Activity"] = physical_activity


        # =================================================
        # ONE-HOT ENCODING
        # =================================================

        if parental_involvement == "Low":

            input_data[
                "Parental_Involvement_Low"
            ] = 1

        elif parental_involvement == "Medium":

            input_data[
                "Parental_Involvement_Medium"
            ] = 1


        if resources == "Low":

            input_data[
                "Access_to_Resources_Low"
            ] = 1

        elif resources == "Medium":

            input_data[
                "Access_to_Resources_Medium"
            ] = 1


        if extracurricular == "Yes":

            input_data[
                "Extracurricular_Activities_Yes"
            ] = 1


        if motivation == "Low":

            input_data[
                "Motivation_Level_Low"
            ] = 1

        elif motivation == "Medium":

            input_data[
                "Motivation_Level_Medium"
            ] = 1


        if internet == "Yes":

            input_data[
                "Internet_Access_Yes"
            ] = 1


        if income == "Low":

            input_data[
                "Family_Income_Low"
            ] = 1

        elif income == "Medium":

            input_data[
                "Family_Income_Medium"
            ] = 1


        if teacher == "Low":

            input_data[
                "Teacher_Quality_Low"
            ] = 1

        elif teacher == "Medium":

            input_data[
                "Teacher_Quality_Medium"
            ] = 1


        if school == "Public":

            input_data[
                "School_Type_Public"
            ] = 1


        if peer == "Neutral":

            input_data[
                "Peer_Influence_Neutral"
            ] = 1

        elif peer == "Positive":

            input_data[
                "Peer_Influence_Positive"
            ] = 1


        if disability == "Yes":

            input_data[
                "Learning_Disabilities_Yes"
            ] = 1


        if education == "High School":

            input_data[
                "Parental_Education_Level_High School"
            ] = 1

        elif education == "Postgraduate":

            input_data[
                "Parental_Education_Level_Postgraduate"
            ] = 1


        if distance == "Moderate":

            input_data[
                "Distance_from_Home_Moderate"
            ] = 1

        elif distance == "Near":

            input_data[
                "Distance_from_Home_Near"
            ] = 1


        if gender == "Male":

            input_data[
                "Gender_Male"
            ] = 1


        # =================================================
        # CONVERT TO DATAFRAME
        # =================================================

        input_df = pd.DataFrame(
            [input_data],
            columns=model_columns
        )


        # =================================================
        # PREDICT EXAM SCORE
        # =================================================

        prediction = model.predict(input_df)[0]

        prediction = float(prediction)


        # Keep prediction within a reasonable score range

        prediction = max(0, min(100, prediction))


        # =================================================
        # RECOMMENDATION SYSTEM
        # =================================================

        recommendations = get_recommendations(

            hours=hours,

            attendance=attendance,

            tutoring=tutoring,

            sleep=sleep,

            previous_scores=previous_scores,

            motivation=motivation,

            resources=resources,

            parental_involvement=parental_involvement,

            internet=internet,

            physical_activity=physical_activity,

            extracurricular=extracurricular,

            teacher_quality=teacher,

            peer=peer
        )


        # =================================================
        # SAVE TO SQL SERVER
        # =================================================

        save_prediction(

            hours,

            attendance,

            parental_involvement,

            resources,

            extracurricular,

            sleep,

            previous_scores,

            motivation,

            internet,

            tutoring,

            income,

            teacher,

            school,

            peer,

            physical_activity,

            disability,

            education,

            distance,

            gender,

            prediction,

            recommendations
        )


        # =================================================
        # SHOW RESULT
        # =================================================

        return render_template(

            "result.html",

            prediction=round(prediction, 2),

            recommendations=recommendations

        )


    except Exception as e:

        print("ERROR:", e)

        return render_template(

            "index.html",

            validation_error=
            "An error occurred while processing the prediction: "
            + str(e)

        )


# =========================================================
# PREDICTION HISTORY
# =========================================================

@app.route("/history")
def history():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            ID,
            Hours_Studied,
            Attendance,
            Sleep_Hours,
            Previous_Scores,
            Tutoring_Sessions,
            Physical_Activity,
            Predicted_Score,
            Recommendations,
            Prediction_Date
        FROM StudentPredictions
        ORDER BY ID ASC
    """)

    records = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "history.html",
        records=records
    )


# =========================================================
# DASHBOARD
# =========================================================

@app.route("/dashboard")
def dashboard():

    connection = get_connection()

    cursor = connection.cursor()


    # =====================================================
    # TOTAL PREDICTIONS
    # =====================================================

    cursor.execute("""
        SELECT COUNT(*)
        FROM StudentPredictions
    """)

    total_predictions = cursor.fetchone()[0]


    # =====================================================
    # AVERAGE SCORE
    # =====================================================

    cursor.execute("""
        SELECT AVG(Predicted_Score)
        FROM StudentPredictions
    """)

    average_score = cursor.fetchone()[0]


    # =====================================================
    # HIGHEST SCORE
    # =====================================================

    cursor.execute("""
        SELECT MAX(Predicted_Score)
        FROM StudentPredictions
    """)

    highest_score = cursor.fetchone()[0]


    # =====================================================
    # LOWEST SCORE
    # =====================================================

    cursor.execute("""
        SELECT MIN(Predicted_Score)
        FROM StudentPredictions
    """)

    lowest_score = cursor.fetchone()[0]


    # =====================================================
    # GET ALL PREDICTED SCORES
    # =====================================================

    cursor.execute("""
        SELECT Predicted_Score

        FROM StudentPredictions

        ORDER BY ID
    """)

    score_records = cursor.fetchall()


    predicted_scores = [

        float(row[0])

        for row in score_records

        if row[0] is not None

    ]


    # =====================================================
    # SCORE CATEGORIES
    # =====================================================

    excellent_count = sum(

        1

        for score in predicted_scores

        if score >= 90

    )


    good_count = sum(

        1

        for score in predicted_scores

        if 75 <= score < 90

    )


    average_count = sum(

        1

        for score in predicted_scores

        if 60 <= score < 75

    )


    needs_improvement_count = sum(

        1

        for score in predicted_scores

        if score < 60

    )


    cursor.close()

    connection.close()


    # =====================================================
    # SEND DATA TO DASHBOARD
    # =====================================================

    return render_template(

        "dashboard.html",

        total_predictions=total_predictions,

        average_score=(

            round(float(average_score), 2)

            if average_score is not None

            else 0

        ),

        highest_score=(

            round(float(highest_score), 2)

            if highest_score is not None

            else 0

        ),

        lowest_score=(

            round(float(lowest_score), 2)

            if lowest_score is not None

            else 0

        ),

        predicted_scores=predicted_scores,

        excellent_count=excellent_count,

        good_count=good_count,

        average_count=average_count,

        needs_improvement_count=needs_improvement_count

    )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )