age = int(input("How old are you?"))

if age >= 18:
    print("It's allowed to drink!")
else:
    print("Try again in:", 18 - age, "years")

drink = "Milk"

if drink == "Coffee":
    print("I love coffee!")
elif drink == "Soda" or drink == "Wine":
    print("I don't like soda or wine!")
else:
    print("I like to drink", drink)

message = "Allowed!" if age >= 18 else "Not allowed!"
print(message)