from typing import Tuple

def bezout( a: int, b: int ) -> Tuple[int, int, int]:
    q = a // b
    r = a % b
    if (r == 0):
        return ( b, 0, 1 )
    if (b % r == 0):
        return ( r, 1, -q )    
    d, alpha, beta = bezout( b, r )
    return d, beta, alpha - beta * q

print( bezout(10, 5))
    