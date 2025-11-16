def create_study_plan(subject: str, hours: int):
    return {
        "subject": subject,
        "total_hours": hours,
        "plan": [
            f"Study {subject} for {hours // 2} hours - Basics",
            f"Study {subject} for {hours // 2} hours - Practice"
        ]
    }
