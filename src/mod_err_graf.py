#! /usr/bin/python

from modulo_error import error
from math import *
from matplotlib.pylab import *
import matplotlib.pyplot as pl

l=[('(a*b)**3','a**3*b**3'),
('a/b','1/(b/a)'),
('exp(a+b)','exp(a)*exp(b)'),
('log(a**b)','b*log(a)'),
('a-b','-(b-a)'),
('(a*b)**4','a**4*b**4'),
('(a+b)**2','a**2+2*a*b+b**2'),
('(a+b)*(a-b)','a**2-b**2'),
('log(a*b)','log(a) + log(b)'),
('a*b','exp(log(a) + log(b))'),
('1/((1/a)+(1/b))','a*b/(a+b)'),
('a*((sin(b))**2+(cos(b))**2)','a'),
('sinh(a+b)','(exp(a)*exp(b)-exp(-a)*exp(-b))/2'),
('tan (a+b)','(sin(a+b))/(cos(a+b))'),
('sin(a+b)','sin(a)*cos(b)+sin(b)*cos(a)')]

def evalua(expr,a,b):
  return eval(expr)

a=0
b=100
n=50
nombre='tabla.txt'

umbral=[1.e-2,1.e-10,1.e-30,1.e-100,1.e-500]

if __name__=='__main__':  
  try:
    fichero=open(nombre,'w')
    for elem in l:
      fichero.write ('%s\n' %(elem[0]))
      fichero.write ('%s\n' %(elem[1]))
      for u in umbral:
	fichero.write ('%5.2f\n' %(error(elem[0],elem[1],a,b,n,u)))
    fichero.close()
  except IOError:
    print 'El fichero no existe'
  
  try:
    fichero=open(nombre,'r')
    for i in range(15):
      expr1=fichero.readline()
      expr2=fichero.readline()
      e=[]
      for j in range(5):
	e.append(float(fichero.readline()))
    
      diagrama1 = pl.figure(1)
      pl.subplot(211)
    
      subplot(2, 1, 1)
      t=linspace(0,3,51)
      y1 = evalua(expr1,t,t)
      y2 = evalua(expr2,t,t)
    
      plot(t,y1,'r-', t, y2, 'bo')
      xticks(range(3))
      legend([expr1, expr2],'best')

      # para trazar en la segunda 
      pl.subplot(212)

      # Lista con los valores de x
      x = [1,2,3,4,5]
      xticks(x,['1.e-2','1.e-10','1.e-30','1.e-100','1.e-500'])
      
      # Lista con los valores de f(x)
      y = e

      pl.plot(x,y,'ro')
      # mostrar por la consola el resultado
      xlim(0,6)
      ylim(0,100)
      pl.show()
    
    fichero.close()
  except IOError:
    print 'El fichero no existe'
 