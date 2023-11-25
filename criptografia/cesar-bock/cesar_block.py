from typing import List
from functools import reduce

class CesarBlock:
    base: int
    text_ascii: List[int]
    text: str
    block_length: int
    __key: int
    __blocks: List[int]
    __mod: int

    def __init__( self, text_file_path: str, length: int, key: int, base: int = 256 ):
        self.base = base
        self.text_ascii = []
        self.text = ''
        self.block_length = length
        self.__mod = self.base ** self.block_length
        self.__key = key % self.__mod
        self.__blocks = []
        with open( text_file_path, 'r' ) as file:
            self.text = file.read()
        self.text_ascii = [ ord(x) for x in self.text ]
    
    def split_into__blocks( self ) -> List[int]:
        self.__blocks = []
        n = len( self.text_ascii )
        q = n // self.block_length
        r = n % self.block_length
        
        def ascii_to_base( k: int, length: int ) -> int:            
            return sum( map( lambda i: self.text_ascii[ k * self.block_length + i ] * ( self.base ** ( self.block_length - 1 - i ) ), range( length ) ) )
        
        self.__blocks = [ ascii_to_base( k, self.block_length ) for k in range(q) ]
        if r > 0:
            self.__blocks.append( ascii_to_base( q, r ) )
        
        return self.__blocks
    
    def encrypt_str( self ) -> str:
        self.split_into__blocks()
        sum_key = ( lambda x : ( x + self.__key ) % self.__mod )
        to_base_ = ( lambda x: self.to_base( x ) )
        to_str = lambda l: ''.join([ chr(i) for i in l ])
        def compose( f, g ):
            return lambda x: f(g(x))
        
        f = reduce( compose, [ to_str, to_base_, sum_key ] )
        return ''.join([ f(x) for x in self.__blocks ])

    def encrypt( self ) -> List[int]:
        self.split_into__blocks()
        sum_key = ( lambda x : ( x + self.__key ) % self.__mod )
        self.__blocks = [ sum_key( x )  for x in self.__blocks ]
        return self.__blocks
    
    def decrypt( self ) -> str:
        assert self.__blocks
        subtract_key = ( lambda x : ( x - self.__key ) % self.__mod )
        to_base_ = ( lambda x: self.to_base( x ) )
        to_str = lambda l: ''.join([ chr(i) for i in l ])
        def compose( f, g ):
            return lambda x: f(g(x))
        f = reduce( compose, [ to_str, to_base_ , subtract_key ])
        return ''.join([ f(x) for x in self.__blocks ])



    def to_base( self, num: int, acc: List[int] = [] ) -> List[int]:
        assert ( num < self.base ** self.block_length )
        
        acc_ = acc.copy()
        if 0 <= num < self.base:
            acc_.insert( 0, num )
            if ( len( acc_ ) ) < self.block_length:
                d = self.block_length - len( acc_ )
                acc_ = [ 0 for _ in range(d) ] + acc_
            return acc_
        q = num // self.base
        r = num % self.base
        acc_.insert( 0, r )
        return self.to_base( q, acc_ )

if ( __name__  == '__main__' ):    
    cesar = CesarBlock( 'texto.txt', 4, 10**4 )    
    print( cesar.encrypt() )
    print( cesar.decrypt() )
    



