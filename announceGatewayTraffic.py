import json
import subprocess
import argparse
from xml.dom import minidom


''' Get programm args '''
parser = argparse.ArgumentParser()
parser.add_argument('-b', '--batman', action='store', help='bat device', default='bat0')

args = parser.parse_args()
argsDir = vars(args)

batDev = argsDir['batman']

''' load traffic stat '''
statXML = subprocess.check_output(["vnstat","-i","eth0", "--xml"])


''' process traffic stat '''
dom = minidom.parseString(statXML)

months = dom.getElementsByTagName('months')[0].childNodes
days = dom.getElementsByTagName('day')[0].childNodes
hours = dom.getElementsByTagName('hour')[0].childNodes

for month in months:
	if month.nodeType == month.ELEMENT_NODE:
		print month


