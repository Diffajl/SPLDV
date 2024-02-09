# SPLDV MEMAKAI LIBLARY NUMPY

import numpy as np

print("Persamaan Linear Dua Variabel")
print("ax + by = c")
print("")
print("\t")
print("Persamaan 1 (ax + by = c)")
a = float(input("Masukan A : "))
b = float(input("Masukan B : "))
c = float(input("Masukan C : "))
print("\t")
print("Persamaan 2 (px + qy = r)")
p = float(input("Masukan P : "))
q = float(input("Masukan Q : "))
r = float(input("Masukan R : "))

A = np.array([[a,b],
              [p,q]])

B = np.array([[c],
              [r]])

A_invers = np.linalg.inv(A)
Z = np.linalg.solve(A,B)
print(f"Solusi : {Z}")