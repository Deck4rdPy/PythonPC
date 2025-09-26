n = int(input("Количество мостов: "))
parts = input('Высоты мостов через пробел: ').split()
heights = []

for i in range(n):
    heights.append(int(parts[i]))

bus_height = 437
crash = False
i = 0

while i < n and not crash:
    if heights[i] <= bus_height:
        print("Crash", i + 1)
        crash = True
    i += 1

if not crash:
    print("No crash")




'''n = int(input("Количество мостов: "))

parts = input('Высоты мостов через пробел: ').split()
heights = []

for i in range(n):
    heights.append(int(parts[i]))

bus_height = 437
crash = False

for i in range(n):
    if heights[i] <= bus_height:
        print("Crash", i + 1)
        crash = True
        break

if not crash:
    print("No crash")'''
