print ("Belajar Bang")
Tinggi = ['Ryan',1.72 , 'Akbar' , 1.75]
print (Tinggi)
Berat = [55 , 50.5 , 60.7 , 75.5]
print (Berat)

import numpy as np

a = np.array([1,2,3,4,5])
b = [1,2,3,4,5]

print(a)
print(b)

np_height = np.array([1.84, 1.79, 1.82, 1.9, 1.8])
print(np_height)

np_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np_2d)

coba = np.array([[1,2,3,4,5], [6,7,8,9,19]])
print(coba)

print(np_2d.shape)

import pandas as pd

Tab = pd.read_csv(r'D:/Pembelajaran Mesin/Tab.csv')
print(Tab["Negara"])
print(Tab.Ibukota)

import matplotlib.pyplot as plt

year = [1980, 1990, 2000, 2010, 2020]
price = [4.5, 10, 8.5, 14.6, 25.8]

print(plt.plot(year, price))
print(plt.show())

print(plt.scatter(year, price))
print(plt.show())

print(plt.bar(year , price))
print(plt.show())