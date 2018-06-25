import urllib.request
import configparser
import json
import bz2

config = configparser.ConfigParser()
config.read('config.ini')


def update_db():
    """Download the PhishTank URLs database in lib/files/database_phishtank.json."""
    api_key = config.get('phishtank', 'api_key')
    api_url = 'http://data.phishtank.com/data/%s/online-valid.json.bz2' % (api_key)
    compraw = urllib.request.urlopen(api_url).read()
    rawdecomp = bz2.decompress(compraw)
    database = json.loads(rawdecomp.decode('utf-8'))
    with open('lib/files/database_phishtank.json', 'w') as outfile:
        json.dump(database, outfile)
