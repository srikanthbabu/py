"""
Helper function to get mutual fund value
Author: Srikanth Babu
Date: 2025-08-06
"""
import re
import requests


def get_nippon_smallcap_nav():
    """
    To get nav values from amfiindia
    """
    url = "https://www.amfiindia.com/spages/NAVAll.txt"
    response = requests.get(url, timeout=10)
    data = response.text

    # Search for the specific scheme name
    pattern = re.compile(
        r"Nippon India Nifty Smallcap 250 Index Fund - Direct Plan "
        r"\(G\).+?;(.+)",
        re.IGNORECASE
        )
    pattern = re.compile(r"Nippon India Nifty Smallcap 250 .+?;(.+)",
                         re.IGNORECASE)
    match = pattern.search(data)

    if match:
        nav = match.group(1).strip()
        return nav.split(';')[0]

    print("NAV not found. Scheme name might have changed or is unavailable.")
    return None


if __name__ == "__main__":
    print(get_nippon_smallcap_nav())
