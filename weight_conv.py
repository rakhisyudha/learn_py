weight = int(input('Weight :'))
unit = input('(L)bs or (k)g: ')
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You're {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You're {converted} lobs")