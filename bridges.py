n = int(input("количество мостов: "))

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
    print("No crash")
