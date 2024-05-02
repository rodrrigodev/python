list = [45, 69, 365, 4, 213]

for number in list:
    print(number)

tuples = (12, 56, 52, 66, 2)
for num in tuples:
    print(num)

person = {"name": "Rodrigo", "city": "Bahia", "age": 25}
for key in person.keys():
    print(key)


for value in person.values():
    print(value)


for key, value in person.items():
    print(f"{key}: {value}")


for num in range(6):
    print(num)

print(list)

for i in range(0, len(list)):
    if i == 1:
        list[i] = 1222

print(list)

letters = ["a", "b", "c", "d", "e"]
for index, value in enumerate(letters):
    print(f"{index}: {value}")