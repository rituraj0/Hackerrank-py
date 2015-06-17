"""
 ('3'.zfill(8) + 'blind'.rjust(8) + 
 	'mice'.ljust(8, '.')).center(40)
'        00000003   blindmice....        '
"""

x=int( raw_input() );

print( bin(x)[2:] )
print( hex(x)[2:] )
print( oct(x)[1:] )

#{} places a variable into a string

def 