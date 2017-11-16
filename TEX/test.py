from numpy import *
from matplotlib.pyplot import *
"""
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

def a(li,lj,ti,tj):
	return (ti-tj)/((1./li**-1) - (1./lj**-1))

print "-------------------"
print "-------------------"

b=a(60 ,100,2.30,2.29)+a(60 ,140,2.30,2.28)+a(60 ,200,2.30,2.27)+a(100,140,2.29,2.28)+a(100,200,2.29,2.27)+a(140,200,2.28,2.27)
print b/6 
a_average = abs(b/6)


print (2.29 - (2./log(1 + sqrt(2))))/(1./(100**-1))

print "-------------------"
print "-------------------"

def t_c_infty(li,tc,a):
	return tc -  (a/float(li))

print 
print 60,t_c_infty(60 ,2.30,a_average)
print 100,t_c_infty(100,2.29,a_average)
print 140,t_c_infty(140,2.28,a_average)
print 200,t_c_infty(200,2.27,a_average)
"""



plot([1./60,1./100,1./140,1./200],[2.30,2.29,2.28,2.27],"ro",label="$T_C$ for finite lattice")
polynomal = polyfit([1./60,1./100,1./140,1./200],[2.30,2.29,2.28,2.27],1)
plot([0,1./60],[polynomal[1],polynomal[0]*1./60+polynomal[1]],label="Polynomial fit")
print polynomal
legend(loc="best")
ylabel("$T_C$",fontsize=20)
xlabel("1/L",fontsize=20)
grid("on")
savefig("polyfit.pdf")
show()
show()