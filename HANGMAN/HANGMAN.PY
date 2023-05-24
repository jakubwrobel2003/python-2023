import math
import random

word_list = ["ardvark", "baboon", "camel"]
word_count = len(word_list)
random_number = random.randint(0, word_count-1)
word = word_list[random_number]
long_of_word = len(word)
print("HANGMAN")
your_word = []
lose_point=0
lose = False
win = False
lose_point=0
max=0
temp=long_of_word

for x in range(0, long_of_word):
    your_word.append("_ ")

while ( win==False or lose==False):
    your_word_two=""
    leter = input("Print a leter ")
 
    table_of_leter = []
    table_of_leter.append(leter)
    z=0
    
    while z<=long_of_word-1:
        sum=0
        y=0

        if word[z] == leter:
            
            your_word[z] = leter

        while y<=long_of_word-1:

            if your_word[y]==word[y] and your_word[y]!="_ ":

                sum=sum+1
               
            y=y+1
       
        temp=long_of_word  
        your_word_two=your_word_two+your_word[z]

        z=z+1
    
    if sum==max:
        lose_point=lose_point+1    
    print(your_word_two)
    if sum==temp:
        print("You win")
        win=True
        break

    max=sum    
    
    if lose_point==7:    
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print(" |   |")
        print("/|\  |")
        print("/ \  |")
        print("     |")
        print("=========")
        print("You lose")
        break
    if lose_point==6:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print(" |   |")
        print("/|\  |")
        print("/    |")
        print("     |")
        print("=========")
    
    if lose_point==5:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print(" |   |")
        print("/|\  |")
        print("     |")
        print("     |")
        print("=========")

    
    if lose_point==4:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print(" |   |")
        print("/|   |")
        print("     |")
        print("     |")
        print("=========")
    
    if lose_point==3:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print(" |   |")
        print(" |   |")
        print("     |")
        print("     |")
        print("=========")
    
    if lose_point==2:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print(" |   |")
        print("     |")
        print("     |")
        print("     |")
        print("=========")

    if lose_point==1:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("=========")

    if lose_point==0:
        print(" +---+")
        print(" |   |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("=========")
    
