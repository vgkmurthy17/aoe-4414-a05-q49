# pool_ops.py
#
# Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p
# This program determines an average pooling layer's output shape & operation count 

# Parameters:
# c_in: count for input channel
# h_in: count for input height 
# w_in: count for input width
# h_pool: count for avg pooling kernel height 
# w_pool: count for avg pooling kernel width 
# s: stride of avg pooling kernel
# p: amount of padding on every input map slide

# Output:
# c_out:  count for output channel 
# h_out:  count for output height 
# w_out:  count for output width
# adds:   # of additions
# muls:   # of multiplications
# divs:   # of divisions 
#
# Written by Vineet Keshavamurthy
#math and sys import
import math 
import sys 

R_E_KM = 6378.137
E_E    = 0.081819221456


# initialize input variables
c_in = float('nan') 
h_in = float('nan') 
w_in = float('nan') 
h_pool = float('nan')
w_pool = float('nan')
s = float('nan')
p = float('nan')
# check for correct amount of arguments
if len(sys.argv) == 8:
  c_in = int(sys.argv[1])
  h_in = int(sys.argv[2])
  w_in = int(sys.argv[3])
  h_pool = int(sys.argv[4])
  w_pool = int(sys.argv[5])
  s = float(sys.argv[6])
  p = float(sys.argv[7])
else:
  print(\
    'Usage: '\
    'Incorrect amount of arguments passed. Recheck the command line argument entered.'\
  )
  exit()

# code below 

#inner h_out term calculation
h_out_term = p*2+h_in-h_pool
# h_out calculation
h_out = 1+(h_out_term)*(1/s)
# w_out inner term calculation
w_out_term=p*2+w_in-w_pool
# w_out calculation
w_out= 1 + (w_out_term)*(1/s)
# number of additions calculation
adds=(w_pool*h_pool-1)*c_in*h_out*w_out
# number of divisions calculation
divs=c_in*h_out*w_out
# number of multiplications is left as zero
muls=0 
#output channel count should be same as input channel count
c_out=c_in

#final value for output channel
print(int(c_out))
#final value for output height count
print(int(h_out))
#final value for output width count
print(int(w_out))
#final value for the number of additions
print(int(adds))
#final value for the # of muls
print(int(muls)) 
#final value for the # of divisions
print(int(divs)) 