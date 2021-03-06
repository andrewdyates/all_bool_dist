#!/usr/bin/python
"""
BOOL_enum
0:NA, 1:YX, 2:PC, 3:XY, 4:UNL, 5:MX, 6:NC, 7:OR

WEAK_enum
0:NC, 1:AND, 2:RN4C, 3: CN4R, 4:XOR, 5:MIX

TODO: use boolean enumerations and compute hamming distance directly using logical_xor.
"""
import numpy as np
import sys

# this can be removed using 4-bit class enumerations and logical_xor.
d0 = np.array((0,11,22,33,44,55,66,77))
d1 = np.array((12,21,14,41,23,32,34,43,45,54,47,74,56,65,67,76))
d2 = np.array((13,31,15,51,17,71,1,10,24,42,2,20,35,53,37,73,3,30,46,64,4,40,57,75,5,50,6,60,7,70))
d3 = np.array((16,61,25,52,27,72,36,63))
d4 = np.array((26,62))
assert len(d0)+len(d1)+len(d2)+len(d3)+len(d4) == 8*8
assert len(set(d0)|set(d1)|set(d2)|set(d3)|set(d4)) == 8*8
assert not any((set(d0)&set(d1), set(d0)&set(d2), set(d0)&set(d3), set(d0)&set(d4),))
assert not any((set(d1)&set(d2), set(d1)&set(d3), set(d1)&set(d4)))
assert not any((set(d2)&set(d4), set(d2)&set(d4)))
assert not any((set(d3)&set(d4),))



def all_pairs_bool_dist(M=None, verbose=True):
  """Compute boolean class distance between all rows of Bool class enum matrix M."""
  assert M is not None
  shape = M.shape
  DIST = np.ones(shape, dtype=np.int)*-1
  for i,row in enumerate(M):
    if verbose: print >>sys.stderr, "Comparing row %d (of %d)..." % (i, shape[1])
    M10 = row*10 + M
    Z = np.ones(shape)*-1
    Z[np.in1d(M10,d0).reshape(shape)]=0
    Z[np.in1d(M10,d1).reshape(shape)]=1
    Z[np.in1d(M10,d2).reshape(shape)]=2
    Z[np.in1d(M10,d3).reshape(shape)]=3
    Z[np.in1d(M10,d4).reshape(shape)]=4
    assert np.sum(Z==-1) == 0
    DIST[i,] = np.sum(Z,1)
  assert np.sum(DIST<0) == 0
  return DIST

def all_pairs_weak_dist(M=None, verbose=True):
  """Compute weak boolean class distance between all rows of Bool class enum matrix M."""
  assert M is not None
  shape = M.shape
  DIST = np.ones(shape)*-1
  for i,row in enumerate(M):
    if verbose: print >>sys.stderr, "Comparing row %d (of %d)..." % (i, shape[1])
    Z = M != row
    DIST[i,] = np.sum(Z,1)
  assert np.sum(DIST<0) == 0
  return DIST
