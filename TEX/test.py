from numpy import *


E = (16*exp(8) - 16*exp(-8))/( 2*exp(8) + 2*exp(-8) + 12)
print E
print E/4


M = (16 + 8*exp(8))/( 2*exp(8) + 2*exp(-8) + 12)
print M
print M/4

print "-----------------"

E_2 = 2*(64*exp(8) + 64*exp(-8))/( 2*exp(8) + 2*exp(-8) + 12)
print E_2
print E_2/4
C_V = E_2 - E**2
print C_V
print C_V/4



print "-----------------"

M_2 = (32 + 32*exp(8))/( 2*exp(8) + 2*exp(-8) + 12)
print M_2
print M_2/4
chi = M_2 - M**2
print chi
print chi/4




teller_list = zeros(10000)
Mulig_E = linspace(-2,2,10000)
array_med_verdier = []

for value in array_med_verdier:
	for interval in range(len(Mulig_E)):
		if value < Mulig_E[interval]:
			teller_list[interval] += 1












