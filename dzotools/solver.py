# AUTOGENERATED! DO NOT EDIT! File to edit: solver.ipynb (unless otherwise specified).

__all__ = ['Solver']

# Cell
import numpy as np

# Cell
class Solver:
    def __init__(self, A, b):
        self.A = A
        self.b = b

    def relative_accuracy(self, x):
        """Calculate the L2 norm of the residuals and divide by L2 of b"""
        return np.linalg.norm(self.A@x - self.b) /  np.linalg.norm(b)

    @property
    def L(self):
        """Get the lower triangular part of matrix A"""
        return np.tril(self.A, k=-1)

    @property
    def D(self):
        """Create a zero matrix with elements on the diagonal"""
        return np.diag(np.diag(self.A))

    def _solve(self, Q):
        """Solve the Ax=b using a given matrix Q"""
        xk = np.zeros(len(self.b))

        # Maximum number of iterations is limited
        for i in range(1, 10**4):
            xk = np.linalg.inv(Q) @ ((Q-self.A) @ xk + self.b)

            if self.relative_accuracy(xk) < 10**-6:
                return i, xk

        raise LinAlgError("Solution did not converge")

    def solve_jacobi(self):
        Q = self.D
        return self._solve(Q)

    def solve_gauss_seidel(self):
        Q = self.D + self.L
        return self._solve(Q)