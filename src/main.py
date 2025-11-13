def add(a, b):
    return a + b

def is_palindrome(s):
    return s == s[::-1]

if __name__ == "__main__":
    print(add(2, 3))
    print(is_palindrome("radar"))
