import random

game=True
lives=5
wordbank=["apple","banana","cookie","pizza","cake"]
guessed_letters=[]

word=random.choice(wordbank)
hidden=[]

for i in range (len(word)):
  hidden.append("_")

while (game):
  guess=input("Enter a letter.")
  match = False   
      
      for i in range(len(word)):
        if (word[i]==guess):
          hidden[i]=guess
          match=True

      if (match==False):
        print("Incorrect!")
        lives-=1
    
      if (lives==0):
        game=False
        print(f"Game lost! Correct word is {word}")
      elif (word=="".join(hidden)):
          print("You win!")
    
    print("".join(hidden))
    
    
  
  
