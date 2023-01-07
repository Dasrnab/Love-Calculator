print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_in_lower = name1.lower()
name2_in_lower = name2.lower()
#print(name1_in_lower)

name_together = name1_in_lower + ' ' + name2_in_lower
name_together.count("t")
name_together.count("r")
name_together.count("u")
name_together.count("e")

#print(type(name_together.count("t")))
true_in_name_together = name_together.count("t") + name_together.count("r") + name_together.count("u")+ name_together.count("e")

#print(true_in_name_together)
true_in_name_together_string = str(true_in_name_together)

love_in_name_together = name_together.count("l") + name_together.count("o") + name_together.count("v") + name_together.count("e")

love_in_name_together_string = str(love_in_name_together)

#print(love_in_name_together_string)

true_love = true_in_name_together_string + love_in_name_together_string

#print(true_love)
true_love_integer = int(true_love)

if true_love_integer < 10 or true_love_integer > 90:
    print(f"Your score is {true_love},you go together like coke and mentos")
elif true_love_integer >= 40 and true_love_integer <= 50:
    print(f"Your score is {true_love},you are alright together")
else:
    print(f"Your score is {true_love}.") 