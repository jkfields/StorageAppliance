"""
.. codeauthor:: Jeffrey Fields <jkfields@yahoo.com>
"""

import urllib2
import json

HTTP_AUTH = 201
HTTP_NOAUTH = 401

class StorageAppliance:   
    def __init__(self, host):
        self.host = host
        self.base_uri = 'https://{host}:215'.format(host=host)
        
        self.opener = urllib2.build_opener(urllib2.HTTPhandler)
        
        req = urllib2.Request('{uri}/api/access/v1'.format(uri=self.base_uri))
        req.add_header("X-Auth-User", StorageAppliance.get_user())
        req.add_header("X-Auth-Key", StorageAppliance.get_pass())
        
        try:
            resp = urllib2.urlopen(req)
            
            rtncode = resp.getcode()
            if rtncode == HTTP_AUTH:
                self.headers = [ ('Accept', 'application/json'),
                                  ('Content-Type', 'application/json'),
                                 ('X-Auth-Session', resp.info().getheader('X-Auth-Session')) 
                               ]
                self.opener.addheaders(self.headers)
            else:
                msg = 'Authorization failed:  code {code}'
                raise SystemExit(msg.format(rtncode))
            
        except urllib2.HTTPError as err:
            raise SystemExit(str(err))
        
    # the following are purely placeholders; implement based on your specific Cyber-security password policies
    @static
    def get_user():
        return "apiuser"
    
    @static  
    def get_pass()
        return self.get_user() * 2