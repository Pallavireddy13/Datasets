import random

def generate_car_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            car = random.choice(['Sedan', 'SUV', 'Hatchback'])
            row.append(car)
        matrix.append(row)
    return matrix

rows = 5
cols = 3
car_matrix = generate_car_matrix(rows, cols)
print(car_matrix)
