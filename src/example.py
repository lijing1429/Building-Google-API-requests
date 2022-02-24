from datetime import datetime, timedelta

import requests
from pandas._libs.tslibs.timestamps import Timestamp

def create_url(homeaddr, destaddr, isdriving, definetime,APIkey):
    '''use data to create direction url
    Required parameters: origin postcode (uk); destination postcode (uk)
    optional - Drive mode: Default drive mode is transit; Y-driving; N-tansit
    optional - Search time: '''
    homecode = address_coding(homeaddr)
    placementcode = address_coding(destaddr)
    drivemode = drivemode_coding(isdriving)
    timepart = searchtime_coding(definetime)
    url = fr"https://maps.googleapis.com/maps/api/directions/json?origin={homecode}%uk&destination={placementcode}%uk&mode={drivemode}&{timepart}key={APIkey}"
    print(url)
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json() # change expression ---- directionData = json.loads(response.text)

def address_coding(address):
    '''process the origin or destination: using the original data to meet the url's requirement.
    address == any UK postcode. (UK postcode format pattern see link: https://ideal-postcodes.co.uk/guides/uk-postcode-format.)
    '''
    address = address.strip()    
    if len(address) > 3:
        address = address[:-3].replace(" ","").replace(",", "")+" " + address[-3:]
        address = address.replace(" ", "+")
    else:
        address = ""
    return address

def drivemode_coding(isdriving):
    '''process the driving mode: using the original data to meet the url's requirement.
    isdriving == "Y" or "N" or "". Default drive mode is transit; Y-driving; N-tansit 
    '''
    definemode = isdriving.strip().lower()
    if definemode == "y":
        drivemode = "driving"
    elif definemode == "n":
        drivemode = "transit"
    else:
        drivemode = "transit" 
    return drivemode

def searchtime_coding(definetime):
    '''process the searchtim: using the original data to meet the url's requirement.
    definetime == "22/02/2022 09:45:00". definetime could be pandas timestamp format or string or nan.
    if definetime is not nan, then use this time as arrive time. otherwise, the departure time is now.
    '''
    try:               # time data is normal
        searchtime = int(definetime.timestamp())
        timepart = f'arrival_time={searchtime}&'
    except:
        if definetime==definetime and type(definetime)==str and len(definetime.strip()):  # time seems normal, but it has blank() space before or after 
            searchtime = int(datetime.strptime(definetime.strip(), '%d/%m/%Y %H:%M:%S').timestamp())
            timepart = f'arrival_time={searchtime}&'
        
        searchtime = int(datetime.now().timestamp())  # 1. time data just blank() space 2. time data nan 
        timepart = ''

    return timepart
 
if __name__ == "__main__":
  APIkey = {yourkey}
  directiondata = create_url('SW1A 2AD', 'SW1A 2AW', 'N', '07/03/2022 09:30:00', APIkey)
  print(directiondata)