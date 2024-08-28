import math


def binomial_pmf(n, p, k):
    return math.comb(n, k) * p ** k * (1 - p) ** (n - k)


def poisson_pmf(k, lam):
    return ((lam ** k) * (math.e ** -lam)) / math.factorial(k)


def geometric_pmf(n, p):
    return (1 - p) ** (n - 1) * p
