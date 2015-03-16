import xml.etree.ElementTree as etree

n = int( input() )

xml = ""

for i in range(n):
    tp = str( input() )
    xml = xml + tp;

#print(xml)

tree = etree.ElementTree(etree.fromstring(xml))

root = tree.getroot()

ans = 0;

for i in root.iter():
    ans = ans + len( i.attrib);
    
print(ans);
    

#print(tree)
