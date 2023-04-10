import numpy as np
import matplotlib.pyplot as plt


print(f'A = {matrix}')

matrix_dimension = 5
twos = np.ones(5) * 2
print(f'T-array = {twos}')

twos_matrix = np.diagflat(twos)
print(f'T-matrix = {twos_matrix}')
print()

negative_ones = np.ones(4) * -1
print(f'N-array = {negative_ones}')

upper_negative_ones = np.diagflat(negative_ones, 1)
print(f'N-upper = {upper_negative_ones}')

lower_negative_ones = np.diagflat(negative_ones, -1)
print(f'N-lower = {lower_negative_ones}')
print()

matrix = twos_matrix + upper_negative_ones + lower_negative_ones
print(f'M {matrix}')

eigenvalues, eigenvectors = np.linalg.eig(matrix)
print(f'lambda = {eigenvalues}')
print()
print(f'x = {eigenvectors}')
print()

