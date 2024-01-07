def find_palindrome(word):
    lowercase_word = word.lower()
    if len(lowercase_word) <= 1:
        return True
    else:
        return lowercase_word[0] == lowercase_word[-1] and find_palindrome(lowercase_word[1:-1])
    

print(find_palindrome("Racecar"))
print(find_palindrome("Chris"))   
print(find_palindrome("CiVIc"))
print(find_palindrome("a"))
print(find_palindrome(""))
print(find_palindrome("oovoo_oovoo"))

            
#In Python, [::-1] means reversing a string, list, or any iterable with an ordering.   
hello = "hello\n"
print(hello[::-1])


