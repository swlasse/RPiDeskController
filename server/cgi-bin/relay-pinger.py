import cgi
import sys
import subprocess as sp
import json

def ReadGpio(ch) :
        process = sp.Popen(["/usr/local/bin/gpio", "-g", "read", ch], stdout = sp.PIPE)
        data, _ = process.communicate()

        data = str.replace(data, "\r", "")
        data = str.replace(data, "\n", "")

        return data

print "Content-Type: text/html"
print ""

response = {'23' : ReadGpio('23'),
	    '24' : ReadGpio('24')}

print json.dumps(response)
