# Python 3 program to count the uppercase, 
# lowercase, special characters 
# and numeric values 

# Function to count uppercase, lowercase, 
# special characters and numbers 
def Count(str):
        S="AEIOU"
        s="aeiou"
        upper, lower, white_spaces,vowel,consonent = 0, 0, 0, 0,0
        for i in str:
            if i.isupper():
                upper += 1
            elif i.islower():
                lower += 1
            else:
                white_spaces+=1

            if i in S:
                vowel+=1
            elif i in s:
                vowel+=1
            else:
                consonent+=1
        print("no of Uppercase letter:",upper)
        print("no of lowercase letter:",lower)
        print("no of vowels in sring:",vowel)
        print("no of consonent in string:",consonent-white_spaces)
        print("no of white spaces:",white_spaces)
    

# Driver Code
str = "Ansh Maurya"
Count(str)

# This code is contributed 
# by Sushma Reddy
