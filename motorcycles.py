#!/usr/bin/env python
# change the list values

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('Audi')
print(motorcycles)

motorcycles.insert(0, 'hahaha')
print(motorcycles)

del motorcycles[0]
print(motorcycles)
motorcycle_1 = motorcycles.pop()
print(motorcycles)
print(motorcycle_1)