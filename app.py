from fitness_chatbot import chatbot_response
from flask import Flask, render_template, request
import math
import pickle
import numpy as np


app = Flask(__name__)

model = pickle.load(open('calorie_model.pkl', 'rb'))


# ---------------- Calorie Calculation ----------------
def calculate_calories(age, gender, height, weight, activity, goal):
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_map = {'low': 1.2, 'medium': 1.55, 'high': 1.75}
    activity_val = activity_map[activity]

    calories = model.predict([[age, height, weight, activity_val]])[0]
    calories = int(calories)

    

    calories = bmr * activity_map[activity]

    if goal == 'loss':
        calories -= 400
    elif goal == 'gain':
        calories += 400

    return round(calories)
   


# ---------------- Workout Logic ----------------
def workout_plan(goal, gym):
    if goal == 'loss' and gym == 'no':
        return "Home HIIT, skipping, squats, planks (30 min/day)"
    if goal == 'gain' and gym == 'yes':
        return "Gym split workout: Chest, Back, Legs, Shoulders"
    return "Brisk walking, yoga, light strength training"

# ---------------- Diet Logic ----------------
def diet_plan(veg, calories):
    if veg == 'yes':
        return f"Vegetarian Indian diet (~{calories} kcal): Idli/Dosa, Dal, Rice, Paneer, Fruits"
    else:
        return f"Non-Veg Indian diet (~{calories} kcal): Eggs, Chicken, Rice, Chapati, Vegetables"

# ---------------- Routes ----------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    age = int(request.form['age'])
    gender = request.form['gender']
    height = int(request.form['height'])
    weight = int(request.form['weight'])
    activity = request.form['activity']
    goal = request.form['goal']
    gym = request.form['gym']
    veg = request.form['veg']

    calories = calculate_calories(age, gender, height, weight, activity, goal)
    workout = workout_plan(goal, gym)
    diet = diet_plan(veg, calories)

    return render_template('result.html', calories=calories, workout=workout, diet=diet)


@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    reply = ""
    if request.method == 'POST':
        user_msg = request.form['message']
        reply = chatbot_response(user_msg)
    return render_template('chatbot.html', reply=reply)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

