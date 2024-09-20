import random

words = ["apple","pineapple","pool","orange","water","popcorn"]

    #dictionary made here
hangman = { 0: ("   ",
                "   ",
                "   "),
            1:  (" o ",
                 "   ",
                 "   "),
            2:  (" o ",
                 " | ",
                 "   "),
            3:  (" o ",
                 "/| ",
                 "   ",),
            4:  (" o ",
                 "/|\\ ",
                 "   ",),
            5:  (" o ",
                 "/|\\",
                 "/   ",),
            6:  (" o ",
                 "/|\\",
                 "/ \\",)}
    
def display_hangman(wrong_answers):
    print("******************")
    for line in hangman[wrong_answers]:
        print(line)
    print("******************")
    

def display_answer(answer):
    print("correct answer is :")
    print(answer)

def display_hint(hint):
    print(" ".join(hint))

answer=random.choice(words)
def main():    
    hint=["_"]*len(answer)
    wrong_answers = 0
    guessed = set()
    is_running = True
    while is_running:
        display_hangman(wrong_answers)
        display_hint(hint)
        guess=input("Enter your choice : ").lower()
        print()
        #checking weather the entered stuff is a single character
        if len(guess)!= 1 or not guess.isalpha() or guess.isdigit():
            print("Invalid input !!")
            continue
        guessed.add(guess)
        if guess in answer or not guess in guessed:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
                
        else:
            wrong_answers += 1
        
        if wrong_answers>=len(hangman)-1:
            print("You Loose !!")
            is_running=False
            display_hangman(wrong_answers)
            display_answer(answer)
        if "_" not in hint:
            print("Yo U wON!!")
            is_running=False
            display_hangman(wrong_answers)
            print("Your hang man was saved!!")
            

  


if __name__=="__main__":
    main()
