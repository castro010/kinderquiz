
#### Inhoud van `kinderquiz.py`:

```python
import requests
import random

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

def main():
    print("Welkom bij de kinderquiz!")
    
    # Vraag om naam en leeftijd
    naam = input("Wat is je naam? ")
    leeftijd = int(input("Hoe oud ben je? "))
    
    if leeftijd != 4:
        print("Deze quiz is speciaal voor kinderen van 4 jaar oud.")
        return
    
    # Haal vragen op
    vragen = fetch_questions()
    
    if not vragen:
        print("Er zijn geen vragen beschikbaar op dit moment.")
        return
    
    # Shuffle de vragen
    random.shuffle(vragen)
    
    score = 0
    
    # Vraag 4 vragen
    for i in range(4):
        vraag = vragen[i]
        print(vraag["vraag"])
        antwoord = input("Jouw antwoord: ")
        if antwoord.lower() == vraag["antwoord"].lower():
            print("Goed gedaan!")
            score += 1
        else:
            print(f"Helaas, het juiste antwoord is: {vraag['antwoord']}")
    
    # Eindresultaat en prijs
    print(f"Goed gedaan, {naam}! Je hebt {score} van de 4 vragen goed.")
    if score == 4:
        print("Gefeliciteerd! Je wint een gouden ster!")
    else:
        print("Goed geprobeerd! Je krijgt een zilveren ster.")

if __name__ == "__main__":
    main()
