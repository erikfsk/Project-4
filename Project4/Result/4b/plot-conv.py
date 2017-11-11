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



b_4 = get_data("MC100000T1N2.txt")
#plot(sqrt(planet["x"]*planet["x"] + planet["y"]*planet["y"]),"r-",label="r")
plot(linspace(0,100,len(abs(b_4["E/N"]))),b_4["E/N"],"r-")
plot([0,100],[-1.99598208594,-1.99598208594],"g--",linewidth=2)
legend(loc="best")
ylabel("Energy [E/N]")
xlabel("MC cycles [%]")
grid("on")
savefig("energy22.pdf")
show()

plot(linspace(0,100,len(abs(b_4["E/N"]))),b_4["E/N"]+1.99598208594,"r-")
legend(loc="best")
ylabel("Error [$\Delta$E/N]")
xlabel("MC cycles [%]")
grid("on")
savefig("energyerror22.pdf")
show()

#T     E/N       E-var/TT       M/N       M-var/T       Mabs/N       
plot(linspace(0,100,len(abs(b_4["E-var/TT"]))),b_4["E-var/TT"],"r-")
plot([0,100],[0.0320823318643,0.0320823318643],"g--",linewidth=2)
legend(loc="best")
ylabel("|M| [|M|/N]")
xlabel("MC cycles [%]")
grid("on")
savefig("cv22.pdf")
show()

plot(linspace(0,100,len(abs(b_4["E-var/TT"]))),b_4["E-var/TT"]-0.0320823318643,"r-")
legend(loc="best")
ylabel("Error [$\Delta$|M|/N]")
xlabel("MC cycles [%]")
grid("on")
savefig("cverror22.pdf")
show()


#Mabs/N       
plot(linspace(0,100,len(abs(b_4["Mabs/N"]))),b_4["Mabs/N"],"r-")
plot([0,100],[0.998660732749,0.998660732749],"g--",linewidth=2)
legend(loc="best")
ylabel("|M| [|M|/N]")
xlabel("MC cycles [%]")
grid("on")
savefig("mabs22.pdf")
show()

plot(linspace(0,100,len(abs(b_4["Mabs/N"]))),b_4["Mabs/N"]-0.998660732749,"r-")
legend(loc="best")
ylabel("Error [$\Delta$|M|/N]")
xlabel("MC cycles [%]")
grid("on")
savefig("mabserror22.pdf")
show()



#M-var/T    
plot(linspace(0,100,len(abs(b_4["M-var/T"]))),b_4["M-var/T"],"r-")
plot([0,100],[0.00401073951623,0.00401073951623],"g--",linewidth=2)
legend(loc="best")
ylabel("$\chi$ ")
xlabel("MC cycles [%]")
grid("on")
savefig("chi22.pdf")
show()

plot(linspace(0,100,len(abs(b_4["M-var/T"]))),b_4["M-var/T"]-0.00401073951623,"r-")
legend(loc="best")
ylabel("Error [$\Delta \chi$]")
xlabel("MC cycles [%]")
grid("on")
savefig("chierror22.pdf")
show()