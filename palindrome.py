def is_palindrome_v1(s):
    """
    (str) -> bool
    Return True id and only if s is a palindrome

    >>> is_palindrome("noon")
    True
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("dented")
    False
    """
    return reverse(s) == s

def reverse(s):
    """
    (str) -> str
    reterned a reversed version of s

    >>> reverse("hello")
    'olleh'
    >>> reverse("a")
    'a'
    """
    rev = " "
    # for each character in s, add text char to the beginning of rev
    for ch in s:
        rev = ch + rev
    return rev
