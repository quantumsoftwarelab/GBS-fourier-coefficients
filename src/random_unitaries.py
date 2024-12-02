import numpy as np
import math
from scipy import linalg


def haar_measure(n):
    """
    Creates a haar-random unitary matrix
    Credit to: Francesco Mezzadri. How to generate random matrices from the classical compact groups, 2006.
    :param n: size of matrix
    :return: the matrix
    """
    z = (np.random.randn(n, n) + 1j * np.random.randn(n, n)) / math.sqrt(2.0)

    q, r = linalg.qr(z)
    d = np.diag(r)

    ph = np.diag(d / np.absolute(d))

    q = q @ ph @ q
    return q
