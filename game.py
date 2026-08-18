import random

game = True
lives = 5
wordbank = ["apple", "banana", "cookie", "pizza", "cake"]
guessed_letters = []

word = random.choice(wordbank)
hidden = []

for i in range(len(word)):
    hidden.append("_")

while game:
    guess = input("Enter a letter: ")
    match = False
    guessed=False

    for x in guessed_letters:
        if (guess==x):
            guessed=True

    if (guessed==True):
        print("You have already guessed this. Try another letter")

    else:
        guessed_letters.append(guess)
        for i in range(len(word)):
            if word[i] == guess:
                hidden[i] = guess
                match = True

        if match == False:
            print("Incorrect!")
            lives -= 1

        if lives == 0:
            game = False
            print(f"Game lost! Correct word is {word}")
        elif word == "".join(hidden):
            game = False
            print("You win!")

    print("".join(hidden))
