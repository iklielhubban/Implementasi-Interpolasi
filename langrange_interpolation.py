import numpy as np

def lagrange_interpolation(x, x_data, y_data):
    def L(k, x):
        term = [(x - x_data[j]) / (x_data[k] - x_data[j]) for j in range(len(x_data)) if j != k]
        return np.prod(term, axis=0)
    return sum(y_data[k] * L(k, x) for k in range(len(x_data)))

# Contoh penggunaan:
if __name__ == "__main__":
    x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
    y_data = np.array([40, 30, 25, 40, 18, 20, 22, 15])
    x = 17.5
    print("Interpolasi Lagrange pada x =", x, "adalah", lagrange_interpolation(x, x_data, y_data))