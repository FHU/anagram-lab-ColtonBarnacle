def anagram(word1, word2):
    if word1.isspace() or word2.isspace():
        return False
   
    # Removing spaces and converting to lowercase
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    # If lengths are not equal, they cannot be anagrams
    if len(word1) != len(word2):
        return False
    
    # Sorting both strings and comparing
    return sorted(word1) == sorted(word2)

def main():
    # Getting inputs from the user
    word1 = input()
    word2 = input()


    # Displaying the result
    print(anagram(word1,word2))

if __name__ == "__main__":
    main()

    