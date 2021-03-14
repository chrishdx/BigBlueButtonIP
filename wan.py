#!/usr/bin/env python

import netifaces as ni
import os
import time
import yaml
import requests

ni.ifaddresses('ens160')


file_name = '/usr/local/bigbluebutton/bbb-webrtc-sfu/config/default.yml'
with open(file_name, 'r') as f:
    data = yaml.safe_load(f)

gespeicherteLAN = data["localIpAddress"]
aktuelleLAN = ni.ifaddresses('ens160')[ni.AF_INET][0]['addr']

aktuellewan = requests.get('http://ipinfo.io/json').json()['ip']
gespeichertewan = data["freeswitch"]["ip"]
print 'Sys-LAN-IP : ' + aktuelleLAN
print 'BBB-LAN-IP : ' + gespeicherteLAN
def bearbeiten(lokaleip, wanip, datei):

        fin = open(datei, "rt")
        #read file contents to string
        data = fin.read()
        #replace all occurrences of the required string
        data = data.replace(lokaleip, wanip)
        #close the input file
        fin.close()
        #open the input file in write mode
        fin = open(datei, "wt")
        #overrite the input file with the resulting data
        fin.write(data)
        #close the file
        fin.close()

if aktuelleLAN != gespeicherteLAN:
        bearbeiten(gespeicherteLAN,aktuelleLAN,"/etc/network/interfaces")
        bearbeiten(gespeicherteLAN,aktuelleLAN,"/opt/freeswitch/etc/freeswitch/vars.xml")
        bearbeiten(gespeicherteLAN,aktuelleLAN,"/opt/freeswitch/etc/freeswitch/sip_profiles/external.xml")
        bearbeiten(gespeicherteLAN,aktuelleLAN,"/etc/bigbluebutton/nginx/sip.nginx")
        bearbeiten(gespeicherteLAN,aktuelleLAN,"/usr/local/bigbluebutton/bbb-webrtc-sfu/config/default.yml")
        bearbeiten(gespeicherteLAN,aktuelleLAN,"/etc/kurento/modules/kurento/WebRtcEndpoint.conf.ini")
        bearbeiten(gespeicherteLAN,aktuelleLAN,"/lib/systemd/system/dummy-nic.service")
        print time.strftime("%d.%m.%Y %H:%M:%S") + 'IP Adressen wurden geeandert'
        os.system("service networking restart")
        os.system('bbb-conf --clean')
else:
        print time.strftime("%d.%m.%Y %H:%M:%S") + ' keine Aenderungen erfoderlich'
print
print 'Sys-WAN-IP : ' + aktuellewan
print 'BBB-WAN-IP : ' + gespeichertewan
if gespeichertewan != aktuellewan:
        bearbeiten(gespeichertewan,aktuellewan,"/etc/network/interfaces")
        bearbeiten(gespeichertewan,aktuellewan,"/opt/freeswitch/etc/freeswitch/vars.xml")
        bearbeiten(gespeichertewan,aktuellewan,"/opt/freeswitch/etc/freeswitch/sip_profiles/external.xml")
        bearbeiten(gespeichertewan,aktuellewan,"/etc/bigbluebutton/nginx/sip.nginx")
        bearbeiten(gespeichertewan,aktuellewan,"/usr/local/bigbluebutton/bbb-webrtc-sfu/config/default.yml")
        bearbeiten(gespeichertewan,aktuellewan,"/etc/kurento/modules/kurento/WebRtcEndpoint.conf.ini")
        bearbeiten(gespeichertewan,aktuellewan,"/lib/systemd/system/dummy-nic.service")
        print time.strftime("%d.%m.%Y %H:%M:%S") + 'IP Adressen wurden geeandert'
        os.system("/sbin/ip addr del " + aktuellewan + " dev lo")
        os.system("/sbin/ip addr add " + gespeichertewan + " dev lo")
        os.system("service networking restart")
        os.system('bbb-conf --clean')
else:
        print time.strftime("%d.%m.%Y %H:%M:%S") + ' keine Aenderungen erfoderlich'

