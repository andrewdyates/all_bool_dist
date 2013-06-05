import numpy as np
import matrix_io as mio
import sys
from __init__ import *

def main(fname=None, as_rows=True):
  assert fname
  if isinstance(as_rows,basestring) and as_rows.lower() in ('f','false','none'): as_rows = False
  print "Loading boolean class enumeration matrix", fname
  D = mio.load(fname)
  M = D['M']
  if not as_rows:
    print "Computing distance between all pairs of columns..."
    M = np.transpose(M)
  else:
    print "Computing distance between all pairs of rows..."
  DIST = all_pairs_bool_dist(M)
  fname_out = fname+'.booldist.tab'
  print "Saving boolean class distance matrix as", fname_out
  if as_rows:
    ids = D.get('row_ids',None)
    mio.save(DIST, fp=fname_out, row_ids=ids, col_ids=ids, fmt="%d")
  else:
    ids = D.get('col_ids',None)
    mio.save(DIST, fp=fname_out, row_ids=ids, col_ids=ids, fmt="%d")
  return fname_out


if __name__ == "__main__":
  args = dict([s.split('=') for s in sys.argv[1:]])
  print args
  D = all_pairs_bool_dist(**args)
  
