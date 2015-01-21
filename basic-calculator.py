def go(a):
    print("%.2f" % a);
    return;

a=float( input() );
b=float( input() );
go(a+b);
go(a-b);
go(a*b);
go(a/b);
go(a//b);
#print( type(a) == type(b) );