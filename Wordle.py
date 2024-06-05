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
def remove_char_at_index(string, index):
    if index < 0 or index >= len(string):
        raise IndexError("Index out of range")
    
    return string[:index] + "!" + string[index+1:]

gg = 1

file = open("Words.txt", "r")
content = file.readlines()
int = random.randint(0,934)
word = content[int]
secret_word = word.strip("\n")
while(gg):
    great_letters = []
    good_letters = []
    temp_seceret_word = secret_word
    bad = 1
    print("")
    correct_spot = False
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
        elif(user_word[x] == temp_seceret_word[x]):
            great_letters.append(x)
            index = temp_seceret_word.index(user_word[x])
            if(index  >= 0 ):
                temp_seceret_word = remove_char_at_index(temp_seceret_word, index)
            correct_spot = True     
    for x in range(len(secret_word)):
        if(temp_seceret_word.__contains__(user_word[x]) and gg == 1):
                good_letters.append(x)
                index = temp_seceret_word.index(user_word[x])
                if(index  >= 0 ):
                    temp_seceret_word = remove_char_at_index(temp_seceret_word, index)

    print("---------------------------------------------------------------------")
    print_word(user_word, great_letters,good_letters)


