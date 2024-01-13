#6.Write a Python program to test whether a passed letter is a vowel or not.
vowel="aeiouAEIOU"
a=input("Enter character : ")

if a in vowel:
    print(a,"is a vowel character")
else:
    print(a,"is a not vowel character")
