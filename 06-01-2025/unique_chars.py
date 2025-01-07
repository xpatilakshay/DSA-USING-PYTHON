
# 1) Check if string contains all unique characters. 

def unique_chars(s):
    s = s.lower()
    if len(s) == len(set(s)):
        print(f"It has unique characters, Duplicates not occured in a String '{s}'")
    else:
        print(f"It doesn't has unique characters, Some Duplicates occured in a String '{s}'")

unique_chars("Akshay")
unique_chars("akshy")
