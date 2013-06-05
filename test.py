#!/usr/bin/python
import script
from __init__ import *
import matrix_io as mio

def main():
  script.main(fname="D.expr.gold.CLS.apr.19.tab")
  D = mio.load("D.expr.gold.CLS.apr.19.tab")
  CLS = all_pairs_bool_dist(D['M'])
  CHECK = mio.load("gold.R.dists.tab")['M']
  print CLS
  print CHECK
  assert np.all(CLS == CHECK)
  

if __name__ == "__main__":
  main()
