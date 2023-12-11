import random

def welcome_scene():
    print("Välkommen till Murder Mystery!") # Välkommen scen 
    print("Du står framför tre dörrar. Varje dörr har en uppgift.") 
    print("Du har bara tre liv. Förlorar du alla, är spelet över.")

def door_task_1():
    print("Dörr 1: Hitta mördarens egenskaper!")
    traits = ["brunett", "lång", "biffig"]
    
    correct_answers = traits

    attempts = 3
    while attempts > 0:
        answer = input("Vilket hår färg har mördaren?").lower()
        if answer in correct_answers:
            correct_answers.remove(answer)
            print("Rätt svar! Fortsätt till nästa fråga.")

        answer = input("Är han lång eller kort?").lower()
        if answer in correct_answers: 
            correct_answers.remove(answer)
            print("Rätt svar! Fortsätt till nästa fråga.")
        
        answer = input("Är mördaren smal eller biffig?").lower()
        if answer in correct_answers:
            correct_answers.remove(answer)
            print("Rätt svar! Du har klarat uppgifter till dörr 1")

        else:
            print("Fel svar! Du förlorar ett liv.")
            attempts -= 1

    if attempts > 0:
        print("Bra jobbat! Du har hittat mördaren. Du får ett vapen!")
        return True
    else:
        print("Du förlorade alla dina liv. Spelet är över.")
        return False
    
def door_task_2():
    print("Dörr 2: Fälla! Du har triggat en fälla och förlorar ett liv.")
    print("Du måste starta om spelet.")
    return False


def door_task_3():
    print("Dörr 3: Lösa tre uppgifter för att hitta mördaren.")
    tasks = [
        "Använde han pistol?",
        "Åkte han bil?"
    ]

    correct_answers = random.sample(tasks, 2)

    attempts = 3
    while attempts > 0:
        print(f"Uppgift: {tasks[3 - attempts]}")
        answer = input("Ditt svar: ").lower()
        if answer in correct_answers:
            correct_answers.remove(answer)
            print("Rätt svar! Fortsätt till nästa uppgift.")
        else:
            print("Fel svar! Du förlorar ett liv.")
            attempts -= 1

    if attempts > 0:
        print("Bra jobbat! Du har hittat mördaren. Du får ett vapen!")
        return True
    else:
        print("Du förlorade alla dina liv. Spelet är över.")
        return False

def capture_murderer():
    print("Du har fångat mördaren och löst mysteriet. Grattis!")

def main():
    welcome_scene()

    while True:
        print("Du står framför tre dörrar.")
        answer = input("Vilken dörr väljer du? (1, 2 eller 3) ")

        if answer == "1":
            door_1_result = door_task_1()
            if door_1_result:
                break
        elif answer == "2":
            door_2_result = door_task_2()
            if door_2_result:
                break
        elif answer == "3":
            door_3_result = door_task_3()
            if door_3_result:
                break
        else:
            print("Ogiltigt val. Försök igen.")

if __name__ == "__main__":
    main()
