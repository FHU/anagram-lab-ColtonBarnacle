#REMOVE PASS AND FIX THIS FUNCTION
def anagram(word_one, word_two):
    sorted_word_one = sorted(word_one)
    sorted_word_two = sorted(word_two)
  
  
    if sorted_word_one == sorted_word_two:
        return True
    else:
        return False

    

if __name__ == '__main__':
    #REMOVE PASS YOUR CODE GOES HERE
    word_one = input()
    word_two = input()
    

    word_one = word_one.lower().replace(' ','')
    word_two = word_two.lower().replace(' ','')
    print(anagram(word_one, word_two))
    