from random import choice
words=["нгрпнгва", "пврвыпрвввв"]
word=choice(words)

print(word)

def check_letters_in_word(w, d, old):
    ret=""
    for i in range(0, len(w)):
        if w[i] == d:
            ret=ret+d
        else:
            ret=ret+old[i]+"*"
    return ret


new_word=(check_letters_in_word(word, "$", '*************************************'))  
print(new_word)
while True:
    letter=input()

    if (letter in 'йцукенгшщзхъфывапролджэячсмитьбюё') and len(letter)==1:
        new_word=check_letters_in_word(word, letter, new_word)
        print(new_word)
    elif letter=="/restart":
        print("restart")
    elif letter=="/end":
        break
    else:
        print("введите букву или комаенду")
print("end")


