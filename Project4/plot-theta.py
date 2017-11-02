# -*- coding: utf-8 -*-
from matplotlib.pyplot import *
from numpy import *

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
		for identifier in identifiers:
			data[identifier] = array(data[identifier])
	return data



planet = get_data("mercury_8_.txt")
planet2 = get_data("mercury_8.txt")
#plot(sqrt(planet["x"]*planet["x"] + planet["y"]*planet["y"]),"r-",label="r")
plot(arctan2(planet["y"],planet["x"])*(360/(2*pi))*3600,"-",label="Non relativistic correction")
plot(arctan2(planet2["y"],planet2["x"])*(360/(2*pi))*3600,"-",label="Relativistic correction")
xlabel("Year [year$_{Mercury}$]")
ylabel("Arc'' [$\\frac{1}{60^2}^\circ$]")
legend(loc="best")
grid("on")
savefig("test.pdf")
show()