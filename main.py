from random import choice

words=["столл", "стулл"]
all_input_letters=""
word=choice(words)


max_try=len(word)*2

correct_try=0
incorrect_try=0



def check_letters_in_word(w, d, old):
    ret=""
    for i in range(0, len(w)):
        if w[i] == d:
            ret=ret+d
        else:
            ret=ret+old[i]
    return ret

# зв-ки вместо загаданного слова. в нем нету значка $ и кол-во звездочек должно быть большк кол-ва зв-чек
new_word=(check_letters_in_word(word, "$", '*'*100))  

print(new_word)

while correct_try + incorrect_try < max_try:
#while True:
    letter=input()
    if (letter == word) :
        correct_try += 1
        print("вы отгодали слово")
        break
    #делинна введенного слова совпадает или равна длинне загаданного, и это не команда
    elif (len(letter) == len(word)) and letter[0] != "/":   
         incorrect_try += 1
         print("не отгодал")
    if (letter in 'йцукенгшщзхъфывапролджэячсмитьбюё') and len(letter)==1:
        if letter in all_input_letters :
            print("вы уже вводили эту букву")
        else:
            all_input_letters += letter 
            new_word1=check_letters_in_word(word, letter, new_word)
            if new_word==new_word1:
                print("не отгодал")
                incorrect_try += 1
            else: 
                print("отгодал")
                correct_try += 1
            new_word=new_word1
            if "*" not in new_word:
                break
            print(new_word)
    elif letter=="/restart":
        print("restart")
    elif letter=="/end":
        break
    else:
        print("введите букву или комаенду")

if "*" not in new_word:
    print("вы победили")
else:
     print("вы проиграли")   
print("попыток всего", correct_try + incorrect_try)
print("неправильных попыток", incorrect_try)
