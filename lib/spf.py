import dns.resolver
import dns.name
from urllib import parse


class SPFRecord(object):

    def __init__(self, domain):
        self.version = None
        self.includes = []
        self.ip4 = []
        self.ip6 = []
        try:
            self._dns_response = dns.resolver.query(domain, 'TXT')
        except Exception:
            return False
        self.txt_records = [txt.to_text() for txt in self._dns_response]
        for txt in self.txt_records:
            self._parse_txt(txt)

    def _parse_txt(self, txt):
        for entry in txt.split(' '):
            if entry.startswith('v') and '=' in entry:
                self._add_version(entry)
            elif entry.startswith('include') and ':' in entry:
                self._add_include(entry)
            elif entry.startswith('ip4') and ':' in entry:
                self._add_ip4(entry)
            elif entry.startswith('ip6') and ':' in entry:
                self._add_ip6(entry)

    @property
    def ips(self):
        return self.ip4 + self.ip6

    def _add_version(self, entry):
        self.version = entry.split('=')[1]

    def _add_include(self, entry):
        self.includes.append(entry.split(':')[1])

    def _add_ip4(self, entry):
        ip = entry.split(':')[1]
        self.ip4.append(ip)

    def _add_ip6(self, entry):
        ip = entry.split(':')[1]
        self.ip6.append(ip)


def is_expired(domain):
    try:
        dns.resolver.query(domain)
        return False
    except dns.resolver.NXDOMAIN:
        return True
    except Exception:
        return False


def get_spf_record(domain):
    if is_expired(domain):
        return None
    try:
        return SPFRecord(domain)
    except Exception:
        return None


def check_spf(spf, domain):
    for inc_domain in spf.includes:
        try:
            url = parse.urlparse("mail://%s" % inc_domain).netloc
            parent = '.'.join(url.split('.')[-2:])
            if is_expired(parent):
                return False
            else:
                return True
        except Exception:
            return False
    return '?'
