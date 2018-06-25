import configparser
import requests
import json

config = configparser.ConfigParser()
config.read('config.ini')


def google_safebrowsing(url):
    client_id = config.get('safebrowsing', 'client_id')
    version = config.get('safebrowsing', 'version')
    api_key = config.get('safebrowsing', 'api_key')
    platform_types = ['ANY_PLATFORM']
    threat_types = ['THREAT_TYPE_UNSPECIFIED',
                    'MALWARE', 'SOCIAL_ENGINEERING',
                    'UNWANTED_SOFTWARE', 'POTENTIALLY_HARMFUL_APPLICATION']
    threat_entry_types = ['URL']
    api_url = 'https://safebrowsing.googleapis.com/v4/threatMatches:find?key=%s' % (api_key)
    threat_entries = [{'url': url}]
    payload = {
        'client': {
            'clientId': client_id,
            'clientVersion': version
        },
        'threatInfo': {
            'threatTypes': threat_types,
            'platformTypes': platform_types,
            'threatEntryTypes': threat_entry_types,
            'threatEntries': threat_entries
        }
    }
    headers = {'content-type': 'application/json'}
    try:
        response = requests.post(api_url, headers=headers, json=payload).json().get('matches', None)
        if response is not None:
            return True
        else:
            return False
    except Exception:
        return '?'


def phishtank(url):
    with open('lib/files/database_phishtank.json') as db:
        data = json.load(db)
    for d in data:
        if (url == d['url']):
            return True
    return False


def wot(url):
    api_key = config.get('wot', 'api_key')
    api_url = 'http://api.mywot.com/0.4/public_link_json2'
    try:
        response = requests.get(api_url, params={'hosts': url, 'key': api_key}).json()
        return any('blacklists' in val for val in response.values())
    except Exception:
        return False
