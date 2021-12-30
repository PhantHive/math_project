import time
import numpy as np


class IterPower(object):

    def __init__(self, A, eps, nmax):
        self.A = A
        self.eps = eps
        self.nmax = nmax
        self.w = None
        self.c = None
        self.old_w = None
        # generate x vector
        self.x = np.random.random(len(self.A))
        self.diff = None
        self.verif = False
        self.vp = None
        self.proc_time = []
        self.iter_list = []

    def w_sequence(self, k):
        w = (np.linalg.matrix_power(self.A, k) @ self.x) / (
            np.linalg.norm((np.linalg.matrix_power(self.A, k)) @ self.x))
        return w

    def c_sequence(self, w):
        c = self.A @ w
        return c

    def eigvals(self):
        # vals, vec = np.linalg.eig(self.A)

        return self.vp, self.c

    def get_datas(self):
        return self.iter_list, self.proc_time


'''if __name__ == '__main__':
    n = 3
    a = np.random.randint(0, 1000, size=(n, n))
    matA = (a + a.T) / 2
    print(matA)
    IV = IterPower(matA, 10, 100)
    last_diff, nbIter = IV.iter()
    print(last_diff, nbIter)'''
