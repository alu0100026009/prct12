#! /usr/bin/python

import random,sys
from math import *

def error (expr1,expr2,valor_min,valor_max,nro_test,umbral):
  errores=0
  contador=0
  while contador < nro_test:
    a = random.uniform(valor_min, valor_max)
    b = random.uniform(valor_min, valor_max)
    if abs(eval(expr1)-eval(expr2))>umbral:
      errores+=1
    contador+=1
  return (100*errores/nro_test)

if __name__=='__main__':
  if (len(sys.argv)<7):
    print 'La forma de uso es %s expr1 expr2 min_value max_value numero_test umbral.' %(sys.argv[0])
    print 'Se usan los valores por defecto:'
    print '%16s %15s %15s %15s %15s %15s %15s %15s' % (sys.argv[0],'expr1','expr2', 'min_value', 'max_value', 'numero_test', 'umbral', 'fallos')
    print '%16s %15s %15s %15s %15s %15s %15s %15.2f' % (sys.argv[0],'(a*b)**3','(a**3)*(b**3)', '-100.0', '100.0', '500', '1.0 e-10', error('(a*b)**3','(a**3)*(b**3)', -100.0,100.0,500,1.e-10))
    
    print '%16s %15s %15s %15s %15s %15s %15s %15.2f' % (sys.argv[0],'(a/b)','1/(b/a)', '-100.0', '100.0', '500', '1.0 e-10',error('(a/b)','1/(b/a)', -100.0,100.0,500,1.e-10))
  else:
   expr1=(sys.argv[1])
   expr2=(sys.argv[2])
   a=float(sys.argv[3])
   b=float(sys.argv[4])
   n=int(sys.argv[5])
   umbral=float(sys.argv[6])
   print '%16s %15s %15s %15s %15s %15s %15s' % (sys.argv[0],'expr1','expr2', 'min_value', 'max_value', 'numero_test', 'umbral','fallos')
   print '%16s %15s %15s %15.2f %15.2f %15d %15.2f %15.2f' % (sys.argv[0], expr1, expr2 , a, b, n, umbral, error(expr1,expr1,a,b,n,umbral))