import xml.etree.ElementTree as ET


tree = ET.parse('stations.xml')
root = tree.getroot()


#codes en types van elk station
print('Dit zijn de codes en types van de 4 stations:')
for station in root.findall('Station'):
    code = station.find('Code').text
    type = station.find('Type').text
    print(code,'-',type)

print('\n')
#stations met synoniemen
print('Dit zijn de stations met synoniemen:')
for station in root.findall('Station'):
    synoniemen = station.find('Synoniemen')
    if synoniemen is not None:
        for synoniem in synoniemen:
           print(synoniem.text)
            
print('\n')

#langste naam van elk station
print('Dit is de langste naam van elk station:')
for station in root.findall('Station'):
    namen = station.find('Namen')
    lang = namen.find('Lang').text
    code = station.find('Code').text
    print(code,'-', lang)