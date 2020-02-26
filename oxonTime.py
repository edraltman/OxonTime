import requests
from bs4 import BeautifulSoup

def getBuses(stopCode: str):
    """
    www.oxontime.com provides live bus times, but not in a neat format.
    This function queries the real data source (www.buscms.com), cleans up the html table and outputs as JSON

    To find your stopcode, use this page: http://www.oxontime.com/livetimes.shtml?q=
    """
    ### Build request and get html
    params = {
        'clientid': 'Nimbus',
        'stopcode': stopCode,
        'format': 'jsonp',
        'servicenamefilder': '',
        'cachebust': '123',
        'sourcetype': 'siri',
        'requestor': 'Netscape',
        'includeTimestamp': 'true',
    }
    response = requests.get(
        "http://www.buscms.com/api/REST/html/departureboard.aspx",
        params=params,
    )

    # Parse the HTML, then convert just the rows into an array
    soup = BeautifulSoup(response.text, 'html.parser')
    rawBusTimeTable = [[cell.text for cell in row("td")] for row in soup("tr")]

    # Remove empty elements
    rawBusTimeTable = list(filter(None, rawBusTimeTable))

    ### Convert raw list to a dictionary

    # Create empty a list to hold the output data and headers
    busList = []
    headers = ['Service', 'Destination', 'eta']

    for bus in rawBusTimeTable:
        # Create dict with headers
        zipObj = zip(headers, bus)
        busDictionary = dict(zipObj)

        # Get first word of service to just get the bus number.
        shortStr = busDictionary['Service'].split(' ', 1)[0]
        busDictionary['Service'] = shortStr

        # Append to output list
        busList.append(busDictionary)

    # return as list
    return busList
