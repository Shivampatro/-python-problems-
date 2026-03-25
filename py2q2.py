def reversestring(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev