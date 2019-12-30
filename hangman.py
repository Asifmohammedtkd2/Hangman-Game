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

def letters_alphabets(secret_word,wrong_word,guess):
    if str(guess).isdigit()==False:
        alphabets=get_correct_word(secret_word,"","",guess)
    else:
        print("Invalid Input")
   
    chance=len(alphabets[2])
    return [alphabets[0],chance]

if __name__ == "__main__":
    p=0
    k=0
    secret_word=get_secret_word(word_file="/usr/share/dict/words")
    print("\n\t\t GAME START... ")
    list_guess=[]
    while True:
        
        if p==0:
            guess=[]
            get_hide_word(secret_word,guess)
            hide_word=get_hide_word(secret_word,guess)
            print(end="\n")
            print("{}{}".format("    Word :",hide_word))
            p=p+1
            
        elif p>0 and k<3:
            print(secret_word)
            print("    Guess :",end="")
            guess=input()
            if len(guess)<2:
                if guess not in list_guess:
                     for i in guess:
                         list_guess.append(i)    
                     guess=list_guess
                     hide_word=letters_alphabets(secret_word,"",guess)
                     print("{}{}".format("    Word :",hide_word[0]))
                     k=hide_word[1]
                     if secret_word == hide_word[0]:
                         
                         break                
                else:
                    print("Already Guessed")
            else:
                print("Only single letter")
            
      
         





         
