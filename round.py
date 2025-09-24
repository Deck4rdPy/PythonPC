x1 = float(input('Enter x1 '))
y1 = float(input('Enter y1 '))
r1 = float(input('Enter r1 '))

x2 = float(input('Enter x2 '))
y2 = float(input('Enter y2 '))
r2 = float(input('Enter r2 '))

d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

if d < (r1 + r2):
    input('окружности имеют 2 точки пересечения')

elif d == (r1 + r2):
    input('окружности имеют 1 точку пересечения')

elif d > (r1 + r2):
    input('окружности не имеют точкек пересечения')
