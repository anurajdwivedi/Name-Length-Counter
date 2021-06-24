your_name = input("What's Your Full Name?\n")
if len(your_name) < 3:
    print("Name length must be at least 3 Characters")
elif len(your_name) > 50:
    print("Name length must be a maximum of 50 Characters")
    print("Good name length is maximum of 50 Characters")
else:
    print("Your full name length is good.")
print("Your name length is: " + str(len(your_name)))