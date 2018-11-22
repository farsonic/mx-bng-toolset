#!/usr/bin/python
from __future__ import print_function
from pyrad.client import Client
from pyrad import dictionary
from pyrad import packet
import sys

if len(sys.argv) != 7:
  print ("usage: disconnect.py <host> <secret> <session-id>")
  sys.exit(1)

ADDRESS = sys.argv[1]
SECRET = sys.argv[2]
ATTRIBUTES = {"Acct-Session-Id": sys.argv[3]}

client = Client(server=ADDRESS, secret=SECRET, dict=dictionary.Dictionary("dictionary"))
client.timeout = 30
attributes = {k.replace("-", "_"): ATTRIBUTES[k] for k in ATTRIBUTES}
request = client.CreateCoAPacket(code=packet.DisconnectRequest, **attributes)
result = client.SendPacket(request)
print(result.code)
