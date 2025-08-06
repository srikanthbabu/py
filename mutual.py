import requests
import re

def get_nippon_smallcap_nav():
    url = "https://www.amfiindia.com/spages/NAVAll.txt"
    response = requests.get(url)
    data = response.text
    
    # print(data)
    # Search for the specific scheme name
    pattern = re.compile(r"Nippon India Nifty Smallcap 250 Index Fund - Direct Plan \(G\).+?;(.+)", re.IGNORECASE)
    pattern = re.compile(r"Nippon India Nifty Smallcap 250 .+?;(.+)", re.IGNORECASE)
    match = pattern.search(data)
    # print(match)
    if match:
        nav = match.group(1).strip()
        return nav.split(';')[0]
    else:
        print("NAV not found. Scheme name might have changed or is unavailable.")

get_nippon_smallcap_nav()

if __name__ == "__main__":
   
    print(get_nippon_smallcap_nav())
