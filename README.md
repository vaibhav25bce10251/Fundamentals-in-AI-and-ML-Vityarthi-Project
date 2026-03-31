# Simple Student Pass/Fail Predictor

## Project Overview
This project is a basic machine learning application made using Python. It predicts whether a student is likely to pass or fail based on three input factors: study hours, attendance, and assignment score.

The main aim of this project is to understand how machine learning can be used for a simple real-life academic problem.

## Problem Statement
Student performance depends on many factors. In this project, I used a few simple academic indicators to build a model that predicts whether the result will be Pass or Fail.

## Objective
The objective of this project is to apply basic AI/ML concepts such as:
- supervised learning
- classification
- model training
- testing
- prediction

## Features Used
The model takes the following inputs:
- Study hours
- Attendance
- Assignment score

The output is:
- Pass
- Fail

## Algorithm Used
I used **Decision Tree Classifier** for this project. It is simple, beginner-friendly, and suitable for classification tasks.

## Technologies Used
- Python
- Pandas
- Scikit-learn

## Project Files
- `train_model.py` : Python code for loading data, training the model, checking accuracy, and predicting result
- `student_data.csv` : dataset used for training and testing
- `README.md` : project documentation
- `Project_Report.md` : detailed report of the project

## How the Project Works
First, the dataset is loaded from the CSV file. Then the input features and output labels are separated. After that, the data is divided into training and testing sets. The Decision Tree model is trained on the training data. Finally, the model predicts whether a student will pass or fail based on user input.

## How to Run
Install the required library first:

```bash
pip install pandas scikit-learn
