from __future__ import print_function

# Objects & Methods

# upper() method makes uppercase
name = "Scott"
message = "Welcome " + name
print(message.upper())

response = raw_input("What should I do")
response = response.upper()
print("You said: ", response.upper())

# capitalize() makes first letter capital
string = "holiday"
string = string.capitalize()
print(string)

anotherString = "easter"
anotherString = anotherString.upper()
print(anotherString)

# lowercase with lower() method
phrase = "NEW YORK"
phrase = phrase.lower()
print(phrase)

concat = string + ' ' + anotherString
print(concat)

# Exrecise

prompt = raw_input("What's your opinion")
print("You said: ", prompt)

password = "PYTHONCODER"
password = password.lower()
print(password)
