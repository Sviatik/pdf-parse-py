import xml.etree.ElementTree as ET
import os


tree = ET.parse(os.getcwd() + '/azure.pdf')
root = tree.getroot()


print(root.tag)
print(root.attrib)

for child in root[0][:-1]:
    print(child.tag + '\t\tid = ' + child.attrib['id'])
    for textlines in child:
        word = ''
        for text in textlines:
            symbol = text.text
            print textlines[0].tag, symbol
            if symbol == None:
                symbol = ' '

            word += str(symbol)
        print word 

print(root[0])