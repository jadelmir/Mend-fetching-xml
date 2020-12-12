import urllib.parse, urllib.request, urllib.error
import xml.etree.ElementTree as ET
 
url = " https://www.senate.gov/general/contact_information/senators_cfm.xml "
url_to_open = urllib.request.urlopen(url).read()
tree = ET.parse(url_to_open)
root_node = tree.getroot()
 
lst = root_node.findall('comment')
for item in lst:
    print(item)