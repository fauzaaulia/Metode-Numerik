import numpy as np

def lagrange(x, y, x_int):
    """
    Interpolasi nilai menggunakan polinomial Lagrange
     Input:
             x: Array berisi nilai x
             y: Array berisi nilai y
         x_int: Nilai untuk diinterpolasi
     Output:
         y_int: Nilai interpolasi
    """

    n = x.size
    y_int = 0

    for i in range(0, n):
        p = y[i]
        for j in range(0, n):
            if i != j:
                p = p * (x_int - x[j]) / (x[i] - x[j])
        y_int = y_int + p

    return [y_int]

def neville(x, y, x_int):
    """
    Menginterpolasi nilai menggunakan polinomial Neville
     Input:
             x: Array berisi nilai x
             y: Array berisi nilai y
         x_int: Nilai untuk diinterpolasi
     Output:
         y_int: Nilai interpolasi
             q: Koefisien matrix
    """

    n = x.size
    q = np.zeros((n, n - 1))
    # Insert 'y' in the first column of the matrix 'q'
    q = np.concatenate((y[:, None], q), axis=1)

    for i in range(1, n):
        for j in range(1, i + 1):
            q[i, j] = ((x_int - x[i - j]) * q[i, j - 1] -
                       (x_int - x[i]) * q[i - 1, j - 1]) / (x[i] - x[i - j])

    y_int = q[n - 1, n - 1]
    return [y_int, q]
