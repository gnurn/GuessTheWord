
possible = input("type your word: ")
print("//")
print("\\\\")
print("//")
print("\\\\")
print("//")
print("\\\\")
print("//")
print("\\\\")
print("//")
print("\\\\")
print("//")
print("\\\\")
print("//")
print("\\\\")
print("//")
print("\\\\")
print("//")
print("\\\\")
print("//")
print("\\\\")
print("//")
print("\\\\")
print("//")
print("\\\\")


word = list(possible)
lamp = list(possible)
letterlist = ["?" for _ in range(len(word))]
guesscount = 4

def letterguesser():
    global guesscount
    print("You've got "+ str(guesscount)  + " tries left.")
    guess = input("type the letter or word: ")
    fire = "".join(lamp)
    if guess in word:
        character = word.index(guess)
        letterlist[character] = guess
        word[character] = "%"
        print("")
        print(letterlist)
        print("")
        letterguesser()
    elif guess == fire:
        print("")
        print("Your guess "+ "*" + fire + "*" +  " was the word!")
        input()


    elif guess not in word:
        print("")
        print("this letter is not in the word or you can't use it anymore (THIS PROGRAM IS CASE SENSITIVE) ")

        guesscount -= 1
        if guesscount != 0:
            print("")
            print(letterlist)
            print("")
            letterguesser()
        elif guesscount == 0:
            print("")
            input("You lose! ")


print("")
print(letterlist)
print("")

letterguesser()



#   if guess == (''.join(word)[2]):
#word = ["o", "s", "t", "k", "a", "k", "a"]
#https://stackoverflow.com/questions/9551857/showing-or-hiding-an-item-in-a-list-in-python

#https://thispointer.com/python-how-to-check-if-an-item-exists-in-list-search-by-value-or-condition/