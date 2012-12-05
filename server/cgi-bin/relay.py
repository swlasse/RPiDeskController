from subprocess import call
import cgi
import sys

print "Content-Type: text/html"
print ""

arguments = cgi.FieldStorage()

rs_channel = arguments["RS_CHANNEL"].value
rs_bit = arguments["RS_BIT"].value

if (rs_channel != "23" and rs_channel != "24"):
	print "Illegal channel!"
	sys.exit()

if (rs_bit != "0" and rs_bit != "1"):
	print "Illegal bit!"
	sys.exit()

print rs_channel;
print rs_bit;

call(["/usr/local/bin/gpio", "-g", "mode", rs_channel, "out"])
call(["/usr/local/bin/gpio", "-g", "write", rs_channel, rs_bit])
