#!/bin/usr/env python
import ldap, ldif
from StringIO import StringIO

ldap_host = '172.24.25.121'
ldap_port = '390'
conn = ldap.initialize('ldap://%s:%s' %(ldap_host, ldap_port))
user = 'cn=ldaproot'
password = '75tartarugas'

ldif_file = StringIO("""


""")

def ldap_search(realm):
      ldap_filter = '(ou=%s*)' %(realm)
      base = 'dc=unimedbh,dc=com,dc=br'
      conn.bind(user,password)
      print(conn.search_s(base,ldap.SCOPE_SUBTREE,ldap_filter))

#def ldap_create_tree(realm)
#    ldap_create =
