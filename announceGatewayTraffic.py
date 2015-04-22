import json
import subprocess
import argparse
from xml.dom import minidom

class GatewayStat():
	def __init__(self):
		self.hour = []
		self.day = []
		self.month = []

	def dump(self):
		dumpRet = {}
		dumpRet['hour'] = self.hour
		dumpRet['day'] = self.day
		dumpRet['month'] = self.month
		return dumpRet

def getText(nodelist):
	retValue = []
	for node in nodelist:
		if node.nodeType == node.TEXT_NODE:
			retValue.append(node.data)
	return ''.join(retValue)

''' load traffic stat '''
statXML = subprocess.check_output(["vnstat","-i","eth0", "--xml"])


''' process traffic stat '''
gwStat = GatewayStat()
dom = minidom.parseString(statXML)

months = dom.getElementsByTagName('months')[0].childNodes
days = dom.getElementsByTagName('days')[0].childNodes
hours = dom.getElementsByTagName('hours')[0].childNodes

for hour in hours:
	if hour.nodeType == hour.ELEMENT_NODE:
		h = {}
		h['day'] = getText(hour.getElementsByTagName('day')[0].childNodes)
		h['id'] = hour.attributes["id"].value
		h['rx'] = getText(hour.getElementsByTagName('rx')[0].childNodes)
		h['tx'] = getText(hour.getElementsByTagName('rx')[0].childNodes)
		gwStat.hour.append(h)

for day in days:
	if day.nodeType == day.ELEMENT_NODE:
		d = {}
		d['day'] = getText(day.getElementsByTagName('day')[0].childNodes)
		d['month'] = getText(day.getElementsByTagName('month')[0].childNodes)
                d['rx'] = getText(day.getElementsByTagName('rx')[0].childNodes)
                d['tx'] = getText(day.getElementsByTagName('rx')[0].childNodes)
		gwStat.day.append(d)

for month in months:
	if month.nodeType == month.ELEMENT_NODE:
		m = {}
		m['year'] = getText(month.getElementsByTagName('year')[0].childNodes)
		m['month'] = getText(month.getElementsByTagName('month')[0].childNodes)
		m['rx'] = getText(month.getElementsByTagName('rx')[0].childNodes)
		m['tx'] = getText(month.getElementsByTagName('tx')[0].childNodes)
		gwStat.month.append(m)



print json.dumps(gwStat.dump(), separators=(',',':'))
