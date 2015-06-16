def input_long_array():
    inp = str( raw_input() );
    A = inp.split();
    return list(map(int, A));

nm=input_long_array();
n=nm[0];
m=nm[1];

ans=[];

for i in range(n):
	ans.append( tuple( input_long_array() ) );

k=int( raw_input() );

ans=sorted(ans , key=lambda tup: tup[k] );

for i in range(n):
	tp = list( ans[i] );
	for j in range(m):
		print(tp[j]),
	print("\n"),
