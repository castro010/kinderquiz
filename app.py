from flask import Flask, request, jsonify
import requests
import random

app = Flask(__name__)

def fetch_questions():
    url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        questions = []
        for item in data["results"]:
            question = {
                "vraag": item["question"],
                "antwoord": item["correct_answer"]
            }
            questions.append(question)
        return questions
    else:
        print("Er is een probleem met het ophalen van vragen.")
        return []

@app.route('/')
def main():
    naam = request.args.get('naam', 'Gast')
    leeftijd = request.args.get('leeftijd', 4, type=int)
    
    if leeftijd != 4:
        return "Deze quiz is speciaal voor kinderen van 4 jaar oud."
    
    vragen = fetch_questions()
    
    if not vragen:
        return "Er zijn geen vragen beschikbaar op dit moment."
    
    random.shuffle(vragen)
    
    score = 0
    antwoorden = []
    
    for i in range(4):
        vraag = vragen[i]
        antwoorden.append({
            'vraag': vraag["vraag"],
            'juiste_antwoord': vraag["antwoord"]
        })
    
    return jsonify({
        'naam': naam,
        'score': score,
        'antwoorden': antwoorden
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
