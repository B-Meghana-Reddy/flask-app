# BMI Calculator Web App

A simple Flask-based web application that calculates **Body Mass Index (BMI)** from user inputs (weight and height) and categorizes the result into health status ranges.

## Live Demo
Check out the live version of the application here:
**https://bmi-calculator-wnee.onrender.com**

## Features
- User-friendly web interface with **HTML templates** (`index.html` for input, `result.html` for output).
- Calculates BMI from **weight (kg)** and **height (cm)**.
- Categorizes BMI into:
  - Severely Underweight
  - Underweight
  - Healthy
  - Overweight
  - Severely Overweight
- Displays BMI value with **2-decimal precision**.

## Tech Stack
- **Python** (Flask framework)
- **HTML / CSS** for frontend
- **Jinja2** templating (via Flask)
- Deployable using **Render**, **Heroku**, **PythonAnywhere**, etc.

## BMI Categories
| BMI Range   | Category             |
| ----------- | -------------------- |
| ≤ 16        | Severely Underweight |
| 16.1 – 18.5 | Underweight          |
| 18.6 – 25   | Healthy              |
| 25.1 – 30   | Overweight           |
| > 30        | Severely Overweight  |
