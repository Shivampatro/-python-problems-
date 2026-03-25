class InvalidAge(Exception):
    pass

age = int(input())
if age < 0 or age > 120:
    raise InvalidAge
else:
    print("Valid Age")