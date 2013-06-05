import numpy as np
import matrix_io as mio
import sys
from __init__ import *

def main(fname=None, as_rows=True, use_weak=False):
  assert fname
  if isinstance(as_rows,basestring) and as_rows.lower() in ('f','false','none'): as_rows = False
  if not use_weak:
    print "Loading boolean class enumeration matrix", fname
  else:
    print "Loading weak class enumeration matrix", fname
  D = mio.load(fname, dtype=np.int)
  M = D['M']
  # verify that enumeration matrices look credible
  if not use_weak:
    assert np.all(np.in1d(M,np.array([0,1,2,3,4,5,6,7])))
  else:
    assert np.all(np.in1d(M,np.array([0,1,2,3,4,5])))
  
  if not as_rows:
    print "Computing distance between all pairs of columns..."
    M = np.transpose(M)
  else:
    print "Computing distance between all pairs of rows..."

  if not use_weak:
    print "Computing Boolean Class distance"
    DIST = all_pairs_bool_dist(M)
    fname_out = fname+'.booldist.tab'
  else:
    print "Computing Weak Class distance"
    DIST = all_pairs_weak_dist(M)
    fname_out = fname+'.weakdist.tab'

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
  
