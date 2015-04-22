#!/bin/bash

sudo python announceGatewayTraffic.py | gzip | sudo alfred -s 160
