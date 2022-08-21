import random

tries = 10
size = 234936
strs = ["" for x in range(size)]
output = ""
selectedWord = ""
user_Input = ""


def get_word():
    word = strs[random.randint(0, size - 1)]
    return word


print("Welcome to hangman!")
with open('wordlist.txt') as f:
    lines = f.readlines()
    i = 0
    for line in lines:
        strs[i] = line.strip()
        i += 1

selectedWord = get_word()


def check_word():
    if user_Input in selectedWord:
        return True
    else:
        return False


output = len(selectedWord) * "*"

print("The word is " + str(len(selectedWord)) + " letters long.")

while output != selectedWord and tries > 0:
    user_Input = input("Enter letter: ")
    if check_word():
        print("Correct!")
        for i in range(len(selectedWord)):
            if selectedWord[i] == user_Input:
                output = output[:i] + user_Input + output[i + 1:]
        if output == selectedWord:
            print("You win!")
        print(output)
    else:
        print("Wrong!")
        tries -= 1
        print("You have " + str(tries) + " tries left.")
        print(output)
        if tries == 0:
            print("Game over!")
            break
# able to check multiple character input
