import random
def get_secret_word(word_file="/usr/share/dict/words"):
    good_words = []
    with open(word_file) as f:
        for word in f:
            word=word.strip()
            if not word.isalpha():
                continue
            if len(word)<5:
                continue
            if word[0].isupper():
                continue
            good_words.append(word)

        word = random.choice(good_words)
    return word.lower()

def get_hide_word(secret_word,guess):
    list_secret_word=[]
    temp=[]
    for i in secret_word:
        list_secret_word.append(i)
    for i in range(0,len(secret_word)):
         if secret_word[i] in guess:
             temp.append(secret_word[i])
         else:
             temp.append("-")
         letters=''.join(temp)
    return letters

def get_correct_word(secret_word,correct_word,wrong_word,guess):
    hide_word=get_hide_word(secret_word,guess)
    list_wrong_word=[]
    list_correct_word=[]    
    for i in guess:
        if i in secret_word and i not in list_correct_word:
            list_correct_word.append(i)
        elif i not in secret_word and i not in list_wrong_word:
            list_wrong_word.append(i)
    return [hide_word,list_correct_word,list_wrong_word]

def status_message(secret_word, guess):
    guess=[]
    mask_word=get_hide_word(secret_word,guess)
    status_message="""{}{}""".format("     Word :", mask_word)
    return status_message
def play(secret_word,wrong_word,list_guess,guess):
    if len(guess)<2 and str(guess).isdigit()==False:
        if guess not in list_guess:
            for i in guess:
                list_guess.append(i)
                guess=list_guess
                guess_Str = ''.join(map(str, list_guess))
                mask_word=get_correct_word(secret_word,"","",guess)
                if mask_word[0] == secret_word:
                    s="You win"
                    return [s,"a""b""x""z"]
                else:
                    mask="""{}{}{}{}""".format("    Word :",mask_word[0],"    turn left :",4-len(mask_word[2]))
                    return [mask,mask_word[2],list_guess,""]
        else:
            s="Already guessed"
    else:
        s="invalid option"
    return [s,""]
    

if __name__ == "__main__":
    k=0
    secret_word=get_secret_word(word_file="/usr/share/dict/words")
    list_guess=[]
    print(secret_word)
    status=status_message(secret_word,[])
    print(status)
    while True:             
         if  k<5:
            print("    Guess :",end="")
            guess=input()
            h=play(secret_word,"",list_guess,guess)
            print(h[0])
            k=len(h[1])
            k=k+1

      
         





         
