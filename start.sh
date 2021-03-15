#!/bin/bash



line="*/5 * * * * /usr/bin/python /root/.arbeitsverzeichnis/run.py >/dev/null 2>&1"
(crontab -u userhere -l; echo "$line" ) | crontab -u root
