person = {"name": "Rodrigo", "city": "Bahia", "age": 25}
print(person)

print(person["name"])
person["name"] = "Alex"
print(person["name"])


# Removing a key
del person["city"]
print(person)

keys = list(person.keys())
print(keys)
print(keys[0])

values = person.values()
print(values)

items = list(person.items())
print(items)
print(items[0][1])
print(items[1][1])