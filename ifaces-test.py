from pprint import pprint, pformat
from textwrap import indent

import netifaces
import ifaddr

print("================================================================================")
print("Using netifaces-plus")

netifaces_listif = netifaces.interfaces()
print("List of interfaces")
print(indent(pformat(netifaces_listif), '  '))

for iface in netifaces_listif:
    print(f"  Addresses of interface {iface}")
    print(indent(pformat(netifaces.ifaddresses(iface)), '    '))

print("================================================================================")
print("Using ifaddr")

ifaddr_listif = ifaddr.get_adapters()
print("Returned object")
print(indent(pformat(ifaddr_listif), '  '))
print("List of interfaces")
for iface in ifaddr_listif:
    print(indent(iface.name, '  '))
    print(f"  Addresses of interface {iface.name}")
    for ip in iface.ips:
       print(indent(pformat(ip.ip), '    '))

