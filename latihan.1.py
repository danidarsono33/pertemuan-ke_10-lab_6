import math

a = lambda x: x ** 2
b = lambda x, y: math.sqrt(x ** 2 + y ** 2)
c = lambda *args: sum(args) / len(args)
d = lambda s: "".join(set(s))

print('Bagian a')
print(a(5))
print('Bagian b')
print(b(5, 10))
print('Bagian c')
print(c(15))
print('Bagian d')
print(d("abcde"))
