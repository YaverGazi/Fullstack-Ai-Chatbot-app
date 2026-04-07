from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
import requests

app = Flask(__name__)
CORS(app)


waiting_for_answer = False

def process_message(user_input):
    global waiting_for_answer

    user_input = user_input.lower()

    if 'exit' in user_input:
        return "See you !"

    elif any(word in user_input for word in ['hello', 'hi']):
        waiting_for_answer = True
        return "Hello! How are you?"

    elif waiting_for_answer and 'i am fine, thank you' in user_input:
        waiting_for_answer = False
        return "Good"

    elif 'time' in user_input:
        now = datetime.datetime.now()
        return f"Now is {now.hour}:{now.minute}"

    elif 'date' in user_input:
        today = datetime.date.today()
        return f"Today is {today}"

    elif 'weather' in user_input:
        city = 'Bielefeld'
        api_key = 'c648eb8e6735ee5597778421ddc2966e'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=tr'
        response = requests.get(url)
        data = response.json()
 
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"Weather in {city}: {temp}°C, {desc}"
    else:
        return "I am sorry, I don't understand. You can ask something else."

# Flask API endpoint
@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")
    reply = process_message(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)