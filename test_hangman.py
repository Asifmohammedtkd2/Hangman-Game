from hangman import get_secret_word,get_hide_word,get_correct_word,status_message,play

def test_secret_word_no_punctuation():
    with open("/tmp/words.txt","w") as f:
        for i in ["word'one","word_two","wordthree"]:
            f.write(i+"\n")
    selected_word = get_secret_word('/tmp/words.txt')
    assert selected_word == get_secret_word('/tmp/words.txt')

def test_secret_word_atleast_five():
    with open("/tmp/words.txt","w") as f:
        for i in ["wo", "wor", "word", "bigword"]:
            f.write(i+"\n")
    selected_word = get_secret_word('/tmp/words.txt')
    assert selected_word == "bigword"

def test_secret_word_lowercase():
    with open("/tmp/words.txt","w") as f:
        for i in ["Wording", "wOrding", "WORDING", "wording"]:
            f.write(i+"\n")
    selected_word = get_secret_word('/tmp/words.txt')
    assert selected_word == "wording"

def test_secret_word_no_repeat():
    with open("/tmp/words.txt","w") as f:
        for i in ["disaster","recall","advise","national","infrastructure","shots","fired", "federation", "duress"]:
            f.write(i+"\n")
    l = []
    for i in range(3):
        l.append(get_secret_word('/tmp/words.txt'))
    assert len(set(l)) == 3

def test_secret__hide_word__nothing_guesses():
    assert get_hide_word("elephant",'') == "--------"

def test_secret__hide_word__single_guess():
    assert get_hide_word("elephant",["a"]) == "-----a--"
    
def test_secret_get_full_hide_word():
    assert get_hide_word("elephant",["e","l","p","h","a","n","t"]) == "elephant"

def test_secret_hide_word_wrong_guesses():
    assert get_hide_word("elephant",["e","w","r","l","a"]) == "ele--a--"

    
def test_get_correct_letter_guesses():
    secret_word="elephant"
    correct_word=""
    wrong_word=""
    guess=["e","a","l"]
    assert get_correct_word(secret_word,correct_word,wrong_word,guess) == ["ele--a--",["e","a","l"],[]]

    
def test_get_wrong_letter_guesses():
    secret_word="elephant"
    correct_word=""
    wrong_word=""              
    guess=["e","a","l","w","q"]
    assert get_correct_word(secret_word,correct_word,wrong_word,guess) == ["ele--a--",["e","a","l"],["w","q"]]

def test_guess_correct_duplicate_letters():
    secret_word="elephant"
    correct_word=""
    wrong_word=""
    guess=["e","a","l","w","q","e","l","a"]
    assert get_correct_word(secret_word,correct_word,wrong_word,guess) == ["ele--a--",["e","a","l"],["w","q"]]

def test_guess_wrong_duplicate_letters():
    secret_word="elephant"
    correct_word=""
    wrong_word=""
    guess=["e","a","l","w","q","q","w"]
    assert get_correct_word(secret_word,correct_word,wrong_word,guess) == ["ele--a--",["e","a","l"],["w","q"]]
def test_letters_guess_digit():
    secret_word="elephant"
    wrong_word=""
    list_guess=[]
    guess="1"
    assert play(secret_word,wrong_word,list_guess,guess) == ['invalid option', '']
def test_status():
     secret_word="elephant"
     guess=[]
     assert status_message(secret_word,guess) == '     Word :--------'
def test_correct_guess_letter():
    secret_word="elephant"
    wrong_word=""
    list_guess=[]
    guess=["t"]
    assert play(secret_word,wrong_word,list_guess,guess) == ['    Word :-------t    turn left :4', [], ['t'], '']
   
def test_same_guess_letter():
    secret_word="elephant"
    wrong_word=""
    list_guess=["e"]
    guess="e"
    assert play(secret_word,wrong_word,list_guess,guess) == ['Already guessed', '']
def test_guess_two_letter():
    secret_word="elephant"
    wrong_word=""
    list_guess=[]
    guess="el"
    print(guess)
    assert play(secret_word,wrong_word,list_guess,guess) == ['invalid option', '']
    
def test_winner():
    secret_word="elephant"
    wrong_word=""
    list_guess=["e","l","p","h","n","a",]
    guess="t"
    assert play(secret_word,wrong_word,list_guess,guess) == ['You win', "a""b""x""z"]

    






    
    


    


    
    
    
