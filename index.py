import requests
import xml.etree.ElementTree as ET
import usaddress


def fetchXmlData():
    url = "https://www.senate.gov/general/contact_information/senators_cfm.xml"
    # for some reason
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', }
    response = requests.get(url, headers=headers)
    return response.content

def ParseAddress(address , state ):
    # since all the addreses have the same layout 
    address = address.split(" ")
    #split the address into an array
    parsedAddress = [{
        "street": " ".join(address[0:5]),
        "city": " ".join(address[5:7]),
        "state": state,
        "postal": address[-1]
    }]
    return parsedAddress
  
    
def ParseXmlToJson(XML):
    tree = ET.fromstring(XmlData)
    for child in tree:
        address = child[5].text
        state = child[4].text
        ParsedAddress  = ParseAddress(address,state)
        print(ParsedAddress)
       
        tempobj = {
            "firstName": child[2].text,
            "lastName":  child[1].text,
            "fullName": child[0].text,
            "chartId": child[10].text,
            "mobile": child[6].text,
            "address": address
        }
        print(tempobj)
        break

XmlData = fetchXmlData()
ParseXmlToJson(XmlData)






