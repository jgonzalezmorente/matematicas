from typing import List

def to_base( base: int, num: int, acc: List[int] = [] ) -> List[int]:
    assert num >= 0
    if num < base:
        acc.insert( 0, num )
        return acc
    
    c = num // base
    r = num % base

    _acc = acc.copy()
    _acc.insert( 0, r )
    print( f'{ num } = { c }·{ base } + { r }' )
    return to_base( base, c, _acc )

if __name__ == '__main__':

    print( '25636 ->', to_base( 27, 25636 ) )    

