import sys

def energy(x, y):
    a = x * 0.81 * 0.75
    b = y * 0.81 * 0.25 * 0.02
    return a + b
x=sys.argv[1]
y=sys.argv[2]
z=energy(int(x),int(y))
print(z)
