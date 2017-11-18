# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from matplotlib.pyplot import *
from numpy import *
import re
import os

output = Popen(["ls"], stdout=PIPE).communicate()[0]
txtfiles = re.findall(".*\.txt",output,re.IGNORECASE)


def get_data(txtfile):
	with open(txtfile,"r") as infile:
		data = {}
		identifiers = infile.readline().split()
		for identifier in identifiers:
			data[identifier] = []

		lines = infile.readlines()
		for line in lines: 
			values = line.split()
			for identifier,value in zip(identifiers,values):
				data[identifier].append(float(value))
		#for identifier in identifiers:
		#	data[identifier] = array(data[identifier])
	return data


for txtfile in txtfiles:
	data = get_data(txtfile)

	EE = sum(data["EE"])/len(data["EE"])
	E = sum(data["E"])/len(data["E"])
	print "<EE> ", EE
	print "<E> ", E/400
	print sqrt(EE - E*E)/400