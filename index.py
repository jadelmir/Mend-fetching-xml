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
    # init empty arr
    arr = [] 
    # create root of the tree
    tree = ET.fromstring(XmlData)
    # loop over every node AKA member 
    for child in tree:
        try:
            #check if member  is not empty 
            if len(child) > 0 :
                address = child[5].text
                state = child[4].text

                ParsedAddress = ParseAddress(address, state)
                #assign data to the correct formet as requested
                tempobj = {
                    "firstName": child[2].text,
                    "lastName":  child[1].text,
                    "fullName": child[0].text,
                    "chartId": child[10].text,
                    "mobile": child[6].text,
                    "address": address
                }
                #push data to the array
                arr.append(tempobj)
        except ValueError :
            print("missing data in",child)
            pass
      
    
def Main():

    XmlData = fetchXmlData()
    JsonArray = ParseXmlToJson(XmlData)

    print(JsonArray)






