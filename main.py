def check_anagram(word1, word2):
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
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")

    # Checking if inputs are anagrams
    result = check_anagram(word1, word2)

    # Displaying the result
    print(result)

if __name__ == "__main__":
    main()

    