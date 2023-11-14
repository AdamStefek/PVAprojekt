print("Program pro výpočet kvádru a jeho obsahu")

a = float(input("Zadej stranu a: "))
b = float(input("Zadej stranu b: "))
c = float(input("Zadej stranu c: "))

p = 2 *(a*b + b*c + c*a)
v = a*b*c
print(f"Zadaný kvádr má povrch {p} a objem {v}")