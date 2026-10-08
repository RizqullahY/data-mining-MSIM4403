import numpy as np

# Data dari gambar
x = np.array([18, 25, 20, 22, 19, 18, 24, 22, 21, 23])
y = np.array([26, 22, 24, 20, 27, 28, 24, 22, 27, 22])

# 1. Hitung rata-rata
x_bar = np.mean(x)
y_bar = np.mean(y)

# 2. Hitung pembilang dan penyebut
pembilang = np.sum((x - x_bar) * (y - y_bar))
penyebut = np.sum((x - x_bar) ** 2)

# 3. Hitung koefisien regresi b
b = pembilang / penyebut

print(f"X_bar     : {x_bar}")
print(f"Y_bar     : {y_bar}")
print(f"Pembilang : {pembilang:.2f}")
print(f"Penyebut  : {penyebut:.2f}")
print(f"Nilai b   : {b:.4f}")
