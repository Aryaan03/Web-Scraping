import argparse
import urllib.request
import urllib
import sqlite3

def fetch_inc():
    url = ("https://www.normanok.gov/sites/default/files/documents/2024-01/2024-01-10_daily_incident_summary.pdf")
    headers = {}
    headers['User-Agent'] = "Chrome/121.0.6167.140"                          

    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read() 

nc_data = fetch_inc()

import pypdf
from pypdf import PdfReader

reader = PdfReader("D:\Spring4\DE\Assignment_0\summary.pdf")
page = reader.pages[0]
print(page.extract_text()) # Shows the extracted text




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True,
    help="Incident summary url.")
    args = parser.parse_args()
if args.incidents:
    main(args.incidents)
