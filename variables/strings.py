# declaration
full_Name = "Rodrigo Santos"

full_Name_Quotation_Marks = """Rodrigo
dos
Santos"""

full_Name_With_Line_Break = "Rodrigo \
Santos"

first_Name = "Rodrigo"
middle_Name = "Santos"

# format
# print("Nome completo (1a forma):", full_Name)
# print("Nome completo (2a forma):" + full_Name)
# print("Nome completo (3a forma):" + "Rodrigo" + "Santos")
# print("Nome completo (4a forma):" + "Rodrigo", "Santos")
# print("Nome completo (5a forma):", full_Name_Quotation_Marks)
# print("Nome completo (6a forma):", full_Name_With_Line_Break)
# print("Nome completo (7a forma): %s" % full_Name)
# print("Nome completo (8a forma): %s %s" % (first_Name, middle_Name))
# print(f"Nome completo (9a forma): {first_Name} {middle_Name}")
# print("Nome completo (10a forma): {} {}".format(middle_Name, first_Name))

print(full_Name)
print(full_Name.upper())
print(full_Name.capitalize())
print(full_Name.count("o"))
print(full_Name.find("R"))
print(full_Name.encode())
print(full_Name.encode().decode())
print(full_Name.replace("o", "i"))

tel = "(12) 91234-1236"
print(tel.replace("(", "").replace(")", "").replace("-", "").replace(" ", ""))

print("-".join(first_Name))
print(full_Name.split())


crazy_Name = "xRodrigo Santosx"

print(crazy_Name.strip('x'))
print(crazy_Name.rstrip('x'))
print(crazy_Name.lstrip('x'))

print(full_Name.startswith("Rod"))
print(full_Name.startswith("Rd"))

print("dri" in full_Name)
print("drih" in full_Name)
print("drih" not in full_Name)