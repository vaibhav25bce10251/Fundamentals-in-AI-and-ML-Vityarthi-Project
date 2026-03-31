import joblib

# Load model
model, le = joblib.load("student_model.pkl")

# User input
study_hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance: "))
assignment_score = float(input("Enter assignment score: "))

# Prediction
prediction = model.predict([[study_hours, attendance, assignment_score]])
result = le.inverse_transform(prediction)

print("Predicted Result:", result[0])
