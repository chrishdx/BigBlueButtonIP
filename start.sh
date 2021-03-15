#!/bin/bash
cd BigBlueButtonIP
mkdir root/.arbeitsverzeichnis
cp wan.py /root/.arbeitsverzeichnis/
line="*/5 * * * * /usr/bin/python /root/.arbeitsverzeichnis/wan.py >> /var/log/BBB-Dynamic.log"
(crontab -u userhere -l; echo "$line" ) | crontab -u root
