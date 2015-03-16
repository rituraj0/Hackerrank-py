import re
if ( re.match(r"^M{0,3}(C[DM]|D?C{0,3})(X[LC]|L?X{0,3})(I[VX]|V?I{0,3})$" , str( input() ) )):
     print("True");
else:
     print("False");