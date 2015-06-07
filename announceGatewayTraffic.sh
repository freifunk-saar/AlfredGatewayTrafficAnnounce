#!/bin/bash

cd "$(dirname "$0")"

sudo git pull origin master
sudo python announceGatewayTraffic.py | gzip | sudo alfred -s 165
