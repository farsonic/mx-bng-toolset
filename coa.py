#!/usr/bin/python
from __future__ import print_function
from pyrad.client import Client
from pyrad import dictionary
from pyrad import packet
import sys

if len(sys.argv) != 7:
  print ("usage: coa.py <coa> <host> <secret> <session-id> <ingress-policy> <egress-policy>")
  sys.exit(1)

ADDRESS = sys.argv[2]
SECRET = sys.argv[3]
ATTRIBUTES = {"Acct-Session-Id": sys.argv[4]}
ATTRIBUTES["ERX-Ingress-Policy-Name"] = sys.argv[5]
ATTRIBUTES["ERX-Egress-Policy-Name"] = sys.argv[6]

client = Client(server=ADDRESS, secret=SECRET, dict=dictionary.Dictionary("dictionary"))
client.timeout = 30
attributes = {k.replace("-", "_"): ATTRIBUTES[k] for k in ATTRIBUTES}
request = client.CreateCoAPacket(**attributes)
result = client.SendPacket(request)
print(result.code)
