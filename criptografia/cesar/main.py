
from collections import Counter
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
encoding = { k:v for k, v in zip( alphabet, range(27) ) }
decoding = { k:v for k, v in zip( range(27), alphabet ) }

def c_key( key: str, letter: str ) -> int:
    assert key in alphabet and letter in alphabet
    return ( encoding[ letter ] + encoding[ key ] ) % 27

#print(encoding)


message = 'ÑWEWUEPKBNÑUKVKWMQKNÑMEIYWYVLBÑWYAERÑBYKMYBNKBVÑ'
encoded_message = [ encoding[letter] for letter in message ]

counter = Counter( message )
for key in counter.most_common(2):    
     decrypted_message = [ ( x - encoding[ key[0] ] ) % 27 for x in encoded_message ]    
     print( key[0], ''.join([decoding[x] for x in decrypted_message]) )
#print( encoded_message )



    