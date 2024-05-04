#!/usr/bin/python
import urllib.request
import re

def parse_data():
    # read website that has the info
    fp = urllib.request.urlopen("https://app.adventurerscodex.com/share/1d69221ca8bd")
    mybytes = fp.read()
    html_doc = mybytes.decode("utf8")
    fp.close()

    # search website html for current health, total health, and temp HP
    health_nums = re.search(r"<p>HP: (\d+) / (\d+), Temp HP: (\d+)", html_doc).groups()

    return "%s %s %s" % health_nums


