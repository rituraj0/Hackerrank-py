import re

n  = int( input() );

for i in range(n):
    curr= str( input());
    if( re.match(r"[7-9][0-9]{9}$", curr) ): 
        print("YES");
    else:
       print("NO");