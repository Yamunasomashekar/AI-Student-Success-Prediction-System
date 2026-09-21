def get_recommendations(
    hours,
    attendance,
    tutoring,
    sleep,
    previous_scores=None,
    motivation=None,
    resources=None,
    parental_involvement=None,
    internet=None,
    physical_activity=None,
    extracurricular=None,
    teacher_quality=None,
    peer=None
):

    recommendations = []

    if hours < 15:
        recommendations.append(
            "Increase your daily study hours."
        )

    if attendance < 75:
        recommendations.append(
            "Improve your attendance to maintain consistent learning."
        )

    if tutoring < 2:
        recommendations.append(
            "Consider additional tutoring sessions."
        )

    if sleep < 6:
        recommendations.append(
            "Try to get at least 6 hours of sleep regularly."
        )

    if previous_scores is not None and previous_scores < 60:
        recommendations.append(
            "Focus on strengthening your basic concepts."
        )

    if motivation == "Low":
        recommendations.append(
            "Set small daily study goals to improve motivation."
        )

    if resources == "Low":
        recommendations.append(
            "Make better use of available learning resources."
        )

    if parental_involvement == "Low":
        recommendations.append(
            "Discuss your academic progress with your parents or guardians."
        )

    if internet == "No":
        recommendations.append(
            "Use offline study materials such as textbooks and notes."
        )

    if physical_activity is not None and physical_activity < 2:
        recommendations.append(
            "Include some physical activity in your daily routine."
        )

    if extracurricular == "No":
        recommendations.append(
            "Consider participating in suitable extracurricular activities."
        )

    if teacher_quality == "Low":
        recommendations.append(
            "Seek additional academic support when topics are difficult."
        )

    if peer == "Negative":
        recommendations.append(
            "Stay connected with peers who support your academic goals."
        )

    if len(recommendations) == 0:
        recommendations.append(
            "Good job! Keep maintaining your current study habits."
        )

    return recommendations