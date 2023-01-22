#Fungsi dalam library Matematika

# Import library math
import math

# Fungsi math.log()
print(">>> Fungsi math.log()")
x = math.log(8, 2)
y = math.log(81, 3)
z = math.log(10000, 10)
print(x)
print(y)
print(z)

# Fungsi math.sqrt()
print(">>> Fungsi math.sqrt()")
x = math.sqrt(100)
print(x)
y = math.sqrt(2)
print(y)

# Fungsi math.copysign()
print(">>> Fungsi math.copysign()")
x = 10.32
y = -13.87
z = -15
x = math.copysign(x, z)
y = math.copysign(y, z)
z = math.copysign(z, 10)
print(x)
print(y)
print(z)