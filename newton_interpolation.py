import numpy as np

def newton_interpolation(x, x_data, y_data):
    n = len(x_data)
    coef = np.zeros([n, n])
    coef[:,0] = y_data

    for j in range(1, n):
        for i in range(n-j):
            coef[i, j] = (coef[i+1, j-1] - coef[i, j-1]) / (x_data[i+j] - x_data[i])

    def N(x):
        result = coef[0, 0]
        term = 1.0
        for i in range(1, n):
            term *= (x - x_data[i-1])
            result += coef[0, i] * term
        return result

    return N(x)

# Contoh penggunaan:
if __name__ == "__main__":
    x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
    y_data = np.array([40, 30, 25, 40, 18, 20, 22, 15])
    x = 17.5
    print("Interpolasi Newton pada x =", x, "adalah", newton_interpolation(x, x_data, y_data))