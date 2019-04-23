#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, opendj
from stackops import realm
from credentials import tokenid, OamUrl

headers = {"iPlanetDirectoryProAWS": "%s" %(tokenid), "Content-Type": "application/json", "If-None-Match": "*"}
def create_realm(realm):
   body = '{"name": "%s", "parentPath": "/", "aliases": [], "active": true}' %(realm)
   resource = OamUrl + 'realms/%s' %(realm)
   print(resource)
   create = requests.put('%s' %(resource), headers=headers, data=body, verify=False)
   print(create.text)
   return realm

def logout():
   resource = OamUrl + 'sessions/?_action=logout'
   _logout = requests.post('%s' %(resource), headers={"iPlanetDirectoryProAWS": headers['iPlanetDirectoryProAWS']}, verify=False)
   print(_logout.text)
   return _logout.text

create_realm('%s' %(realm))
opendj.ldap_search('%s' %(realm))
logout()
