def is_palindrome_iterative(word):
    if word == "":
        return False

    if word[::-1] == word:
        return True

    return False
