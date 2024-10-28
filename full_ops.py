# full_ops.py

# Usage: python3 full_ops.py c_in n_wv
# Determines a fully connected layer's output shape & operation count

# Parameters:
# c_in: count for input channel 
# n_wv: # of weight vectors

# Output:
# c_out:  count for output channel 
# h_out:  count for output height 
# w_out:  count for output width 
# adds:   # of additions 
# muls:   # of multiplications 
# divs:   # of divisions 
#
# Written by Vineet Keshavamurthy

# import math and sys modules
import math 
import sys

# constants
R_E_KM = 6378.137
E_E    = 0.081819221456

# initialize input variables
c_in = float('nan') 
n_wv = float('nan') 
# check for correct number of arguments passed
if len(sys.argv) == 3:
  c_in = int(sys.argv[1])
  n_wv = int(sys.argv[2])
else:
  print(\
    'Usage: '\
    'Incorrect number of input variables passed. Recheck command line entered.'\
  )
  exit()
#code written here

#value for h_out and w_out is just equal to 1. Set both equal to it.
w_out = 1
h_out = 1

#operation to find number of muls
muls=n_wv*c_in
adds=n_wv*c_in
#divs is just equal to zero
divs=0
#number of input and output channels will remain constant. Set both equal to each other:
c_out = n_wv 

# final value for channel count
print(int(c_out))
# final value for height output count
print(int(h_out)) 
# final value for output width count
print(int(w_out)) 
# final value for # of additions
print(int(adds))
# final value for # of muls
print(int(muls))
# final value for # of divisions
print(int(divs)) 
