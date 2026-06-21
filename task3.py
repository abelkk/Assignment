word = input("enter a word:")
if word == word[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
    for a,e,i,o,u in word:
        if (a,e,i,o,u) in word:
            print("word contains a vowel")
        else:
            print("doesn't have a vowel")