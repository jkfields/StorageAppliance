"""
.. codeauthor:: Jeffrey Fields <jkfields@yahoo.com>
"""

import urllib2
import json

HTTP_OK = 200
REQ_CREATED = 201
REQ_NOAUTH = 401

class StorageAppliance:   
    def __init__(self, host):
        self.host = host
        self.base_uri = 'https://{host}:215'.format(host=self.host)
        self.opener = urllib2.build_opener(urllib2.HTTPhandler)
        
        try:
            req = urllib2.Request('{uri}/api/access/v1'.format(uri=self.base_uri))
            req.add_header("X-Auth-User", StorageAppliance.get_user())
            req.add_header("X-Auth-Key", StorageAppliance.get_pass())
            
            resp = urllib2.urlopen(req)
            rtncode = resp.getcode()
            if rtncode == REQ_CREATED:
                self.session = resp.info().getheader('X-Auth-Session')
                self.headers = [ ('Accept', 'application/json'),
                                  ('Content-Type', 'application/json'),
                                 ('X-Auth-Session', self.session) 
                               ]
                self.opener.addheaders(self.headers)
            else:
                msg = 'Failed to create the session; authorization failed: code {code}'
                raise SystemExit(msg.format(code=rtncode))
            
        except urllib2.HTTPError as err:
            raise SystemExit(str(err))
            
    def get(self, href):
        try:
            req = urllib2.Request(self.base_uri + href)
            resp = self.opener.open(req)
            rtncode = resp.getcode():
            body = json.loads(resp.read())
            return json.dumps(body, sort_keys=True, indent=4)
        
        except urllib2.HTTPError as err:
            raise SystemExit(str(err))
        
    # the following are purely placeholders; implement based on your specific Cyber-security password policies
    @static
    def get_user():
        return "apiuser"
    
    @static  
    def get_pass()
        return self.get_user() * 2 + 'pw'
