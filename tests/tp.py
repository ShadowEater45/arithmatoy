# Aucun n'import ne doit être fait dans ce fichier


def nombre_entier(n: int) -> str:
    return 'S'*n + '0'


def S(n: str) -> str:
    return 'S' + n


def addition(a: str, b: str) -> str:
    a = nombre_entier(a) if type(a) == int else a
    b = nombre_entier(b) if type(b) == int else b
    return 'S' * (a.count('S') + b.count('S')) + '0'


def multiplication(a: str, b: str) -> str:
    a = nombre_entier(a) if type(a) == int else a
    b = nombre_entier(b) if type(b) == int else b
    return 'S' * (a.count('S') * b.count('S')) + '0'


def facto_ite(n: int) -> int:
    r = 1
    for i in range(n):
        r *= i+1
    return r

def facto_rec(n: int) -> int:
    if n == 0:
        return 1
    return facto_rec(n-1) * n


def fibo_rec(n: int) -> int:
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibo_rec(n-1) + fibo_rec(n-2)


def fibo_ite(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def golden_phi(n: int) -> int:
    return (1 + sqrt5(n)) / 2


def sqrt5(n: int) -> int:
    return n ** (1/5)


def pow(a: float, n: int) -> float:
    return a**n
