import xml.etree.ElementTree as etree

def deep( tp):
    ans =0 ;
    for ch in tp:
        ans = max( ans , deep(ch));
    return (ans+1);

n = int( input() )

xml = ""

for i in range(n):
    tp = str( input() )
    xml = xml + tp;

#print(xml)

tree = etree.ElementTree(etree.fromstring(xml))

root = tree.getroot()

print( deep(root)-1);
