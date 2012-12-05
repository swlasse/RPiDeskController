# Raspberry Pi Desk Controller
###### RPiDeskController

## About
This project includes server- and client side code for controlling a height-adjustable desk (basically a relay board) via a web site hosted on the Raspberry Pi.

The client side code:

* Uses knockoutjs for MVVM
* Uses twitter bootstrap for simple markup
* Uses jQuery, e.g., for async invocation of web-services on the RPi

The server side code:

* Is based on Python CGI Scripts
* Uses the gpio program "bundled" with WiringPi to interface with the GPIO pins

## Demo

A screenshot of the client is seen here:

![Raspberry Pi Desk Controller][screenshot]

## Setup

#### Install the [lighty (lighttpd)][4] Web Server

See Mark Ingram's brilliant tutorial on this: [http://markingramuk.wordpress.com/2012/08/12/accessing-gpio-from-a-web-server/][1]

#### Install WiringPi

See the project page's guidlines: [https://projects.drogon.net/raspberry-pi/wiringpi/download-and-install/][2]

#### Setup a WiFi- or Ad-hoc Network

See my own tutorial on this: [http://lcdev.dk/2012/11/18/raspberry-pi-tutorial-connect-to-wifi-or-create-an-encrypted-dhcp-enabled-ad-hoc-network-as-fallback/][3]

#### Deploy Code

For instance:

- Client-side code goes here: `/var/www/rpidc`
- Server-side code goes here: `/var/www/cgi-bin`

[1]: http://markingramuk.wordpress.com/2012/08/12/accessing-gpio-from-a-web-server/
[2]: https://projects.drogon.net/raspberry-pi/wiringpi/download-and-install/
[3]: http://lcdev.dk/2012/11/18/raspberry-pi-tutorial-connect-to-wifi-or-create-an-encrypted-dhcp-enabled-ad-hoc-network-as-fallback/
[4]: http://www.lighttpd.net/

[screenshot]: http://lcdev.dk/wp-content/uploads/2012/12/rpidc-screenshot.png "Raspberry Pi Desk Controller"