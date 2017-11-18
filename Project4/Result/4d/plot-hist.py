# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from matplotlib.pyplot import *
from numpy import *
import re
import os

output = Popen(["ls"], stdout=PIPE).communicate()[0]
txtfiles = re.findall(".*\.txt",output,re.IGNORECASE)


def guassian(x,s=0.1419,m=-1.23740381):
	return (1/(sqrt(2*pi)*s**2))*exp(-0.5*((x-m)/s)**2)

def make_histogram_dict(txtfile):
	E_dict = {}
	E_test_list = []
	with open(txtfile,"r") as infile:
		infile.readline()
		for line in infile:
			E_value = float(line.split()[-2])/400
			E_test_list.append(E_value)
			if E_value in E_dict.keys():
				E_dict[E_value] += 1
			else:
				E_dict[E_value] = 1

	E_list = []
	key_list = sorted(E_dict.keys())
	for key in key_list:
		E_list.append(E_dict[key])

	summen = float(sum(E_list))
	for i in range(len(E_list)):
		E_list[i] = E_list[i]/summen

	return E_test_list,key_list,E_list

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
	m = E/400
	s = sqrt(EE - E*E)/400
	hist_list,x,y = make_histogram_dict(txtfile)
	"""
	plot(x,y,linewidth=2)
	plot(linspace(min(x),max(x),1000),[guassian(i)/700 for i in linspace(min(x),max(x),1000)])
	xlabel('Energy [E/N]',fontsize=20)
	ylabel('Probability [%]',fontsize=20)
	grid("on")
	tight_layout()
	legend(["test","guas"])
	savefig("%s.pdf" % txtfile[:-4])
	show()
	"""

	hist(hist_list,bins=linspace(min(x),max(x),len(x)+0.14*len(x)),histtype="bar", normed=1, color='green')
	plot(linspace(min(x),max(x),1000),[guassian(i,s=s,m=m)/7 for i in linspace(min(x),max(x),1000)],"r--",linewidth=2)
	xlabel('Energy [E/N]',fontsize=20)
	ylabel('Probability [%]',fontsize=20)
	grid("on")
	tight_layout()
	savefig("%s-hist.pdf" % txtfile[:-4])
	show()