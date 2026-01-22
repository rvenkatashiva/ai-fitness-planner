# fitness_chatbot.py
# Simple AI-based fitness chatbot logic

import random

responses = {
    "diet": [
        "Drink plenty of water and include fruits daily.",
        "Avoid junk food and prefer home-cooked meals.",
        "Protein intake is important for muscle recovery."
    ],
    "workout": [
        "Consistency is more important than intensity.",
        "Warm up before workouts to avoid injuries.",
        "Take at least one rest day per week."
    ],
    "motivation": [
        "Small progress is still progress. Keep going!",
        "Discipline beats motivation. Stay consistent.",
        "Your future self will thank you for today’s effort."
    ]
}

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "diet" in user_input or "food" in user_input:
        return random.choice(responses["diet"])
    elif "workout" in user_input or "exercise" in user_input:
        return random.choice(responses["workout"])
    elif "motivate" in user_input or "tired" in user_input:
        return random.choice(responses["motivation"])
    else:
        return "I can help with diet, workout, or motivation. Ask me!"