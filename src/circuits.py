import itertools
import strawberryfields as sf
from strawberryfields.ops import *

import random_unitaries


def run_circuit(n: int, r: float):
    """
    Run a Gaussian Boson Sampling circuit with a random unitary with same squeezing on each mode.

    :param n: number of modes for the circuit
    :param r: squeezing parameter to use for circuit input states
    :return: mu (mean vector) and cov (covariance matrix) of output state
    """

    # create a program (ie circuit) with n modes
    gbs = sf.Program(n)

    # generate random unitary matrix
    unitary = random_unitaries.haar_measure(n)

    # use .context to access the array of different modes
    with gbs.context as q:
        S = Sgate(r)

        # apply squeeze gate to all modes
        for i in range(n):
            S | q[i]

        Interferometer(unitary) | q

    eng = sf.Engine(backend="gaussian")
    results = eng.run(gbs)

    # state is a class for the representation of quantum states using the Gaussian formalism
    state = results.state

    mu = state.means()
    cov = state.cov()

    return mu, cov
