def greeting():
    print("Hi There")


def calculate_pi(digits=5):
    """
    Calculate pi to the specified number of decimal digits using the Chudnovsky algorithm.
    This is one of the fastest converging series for calculating pi.
    
    Args:
        digits: Number of decimal digits to calculate (default 5)
    
    Returns:
        float: Value of pi accurate to the specified digits
    """
    from decimal import Decimal, getcontext
    
    # Set precision high enough for accurate calculation
    getcontext().prec = digits + 10
    
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    # Chudnovsky algorithm
    C = 426880 * Decimal(10005).sqrt()
    K = Decimal(6)
    M = Decimal(1)
    X = Decimal(1)
    L = Decimal(13591409)
    S = Decimal(13591409)
    
    # More iterations for better accuracy
    for i in range(1, digits + 10):
        M = M * (K ** 3 - 16 * K) / ((i) ** 3)
        K += 12
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        
    pi_value = C / S
    return float(pi_value)


def calculate_pi_simple(iterations=1000):
    """
    Calculate pi using the Leibniz formula (simpler but slower convergence).
    Pi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ...)
    
    Args:
        iterations: Number of iterations (default 1000 for ~5 digit accuracy)
    
    Returns:
        float: Approximate value of pi
    """
    pi = 0.0
    for i in range(iterations):
        pi += ((-1) ** i) / (2 * i + 1)
    return 4 * pi