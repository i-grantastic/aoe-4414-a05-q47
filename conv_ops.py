# conv_ops.py
#
# Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filter w_filt s p
#   determines the output shape and operation count of a convolution layer

# Parameters:
#   c_in: input channel count
#   h_in: input height count
#   w_in: input width count
#   n_filt: number of filters in the convolution layer
#   h_filt: filter height count
#   w_filt: filter width count
#   s: stride of convolution filters
#   p: amount of padding on each of the four input map sides

# Output:
#   channel count, height count, width count, number of additions performed,
#   number of multiplications performed, and number of divisions performed
#
# Written by Grant Chapman
# Other contributors: None

# import Python modules
import sys
import math

# initialize script arguments
c_in = float('nan')
h_in = float('nan')
w_in = float('nan')
n_filt = float('nan')
h_filt = float('nan')
w_filt = float('nan')
s = float('nan')
p = float('nan')

# parse script arguments
if len(sys.argv) == 9:
  c_in = int(sys.argv[1])
  h_in = int(sys.argv[2])
  w_in = int(sys.argv[3])
  n_filt = int(sys.argv[4])
  h_filt = int(sys.argv[5])
  w_filt = int(sys.argv[6])
  s = int(sys.argv[7])
  p = int(sys.argv[8])
else:
  print(\
    'Usage: '\
    'python3 conv_ops.py c_in h_in w_in n_filt h_filter w_filt s p'\
  )
  exit()

## script below this line

# height of the output map
h_out = math.floor(((h_in + 2*p - h_filt)/s) + 1)

# width of the output map
w_out = math.floor(((w_in + 2*p - w_filt)/s) + 1)

# number of filters
c_out = n_filt

# total number of multiplications
muls = n_filt*h_out*w_out*c_in*h_filt*w_filt

# total number of additions
adds = n_filt*h_out*w_out*c_in*h_filt*w_filt

# total number of divisions
divs = 0

# print
print(int(c_out))
print(int(h_out))
print(int(w_out))
print(int(adds))
print(int(muls))
print(int(divs))