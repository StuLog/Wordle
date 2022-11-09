import random
from colorama import init, Fore, Back, Style
init(autoreset=True)

def print_word(user_word, Gp,dp):
    x = 0
    for i in user_word:
        if(x in Gp):
            print(Style.BRIGHT + Back.GREEN + str(i) , end = '')
        elif(x in dp):
            print(Style.BRIGHT + Back.YELLOW + str(i), end  ='')
        else:
            print(Style.BRIGHT + Back.LIGHTBLACK_EX+ str(i), end = '')
        x = x+1

gg = 1
file = open("Words.txt", "r")
content = file.readlines()
int = random.randint(0,934)
word = content[int]
secret_word = word.strip("\n")
while(gg):
    great_letters = []
    good_letters = []
    bad = 1
    print("")
    while(bad):
        user_word = input("Please give your 5 letter word: ")
        user_word = user_word.lower()
        if(len(user_word) == 5):
            bad = 0
        else:
            print("Wrong word length")
    print("")
    for x in range(len(secret_word)):
        if(user_word == secret_word):
            gg = 0
            print("You got it!!!")
            break
        elif(user_word[x] == secret_word[x]):
            great_letters.append(x)     
        else:
            if(secret_word.__contains__(user_word[x])):
                    good_letters.append(x)
    print("---------------------------------------------------------------------")
    print_word(user_word, great_letters,good_letters)


