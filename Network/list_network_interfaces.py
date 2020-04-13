# pip install netifaces

import netifaces

interfaces = netifaces.interfaces()
print("Interfaces: {}".format(interfaces))


