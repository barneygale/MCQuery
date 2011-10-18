#!/usr/bin/python
import mcquery
import time

print 'Ctrl-C to exit'

host = raw_input('Host (localhost): ')
port = raw_input('Port (25565): ')

if host == '':
    host = 'localhost'
if port == '': 
    port = 25565
else: 
    port = int(port)



print "Connecting..."
q = mcquery.MCQuery(host, port)
print "Connected."

while True:
    print q.full_stat()
    time.sleep(5)
