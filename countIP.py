def ip_to_int(ip):
    val = 0
    for i, s in enumerate(ip.split('.')):
        val += int(s) * 256 ** (3 - i)
    return val

def int_to_ip(val):
    octets = []
    for i in range(4):
        octets.append(str(val % 256))
        val = val >> 8
    return '.'.join(reversed(octets))

def findIPs(start, end):
    for i in range(ip_to_int(start), ip_to_int(end) + 1):
        yield int_to_ip(i)
        


print ("List of IP addresses: %s " % list(findIPs('192.168.111.232', '192.168.111.234')))
print ("Total IP Addresses are %d " % len(list(findIPs('192.168.111.232', '192.168.111.234'))))
