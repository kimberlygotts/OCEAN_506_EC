# import numpy, os, sys, pickle and argparse

import sys, os
import numpy as np
import pickle
import argparse

# local imports - from test code
sys.path.append(os.path.abspath('../shared'))
import my_module as mymod
from importlib import reload
reload(mymod)

# check output and create if does not exist - this is taken from previous examples 
myplace = 'Ocean_506_EC' 

# input directory
in_dir = '../' + myplace + '_data/'

# make sure the output directory exists
out_dir = '../' + myplace + '_output/'
mymod.make_dir(out_dir)


# make different types of arrays and try out a few things

a=np.array([1,3,7,9])
print(a)
print(a[2])

b=np.full((2,2),5)
print(b)

bb=b/.5
print(bb)

c=np.full((2,2),1)

d=np.append(c,bb)
print(d)
print('size of d')
print(d.shape)

dd=np.sqrt(d)
print(dd)

e=bb/c
print(e)


# save one of your arrays as a pickle file - from test
out_fn = out_dir + 'pickled_array.p'
pickle.dump(d, open(out_fn, 'wb')) # 'wb' is for write binary

# read the array back in
cucumber = pickle.load(open(out_fn, 'rb')) # 'rb is for read binary
print(cucumber)

# argparse - this is a more difficult module - use the argparse tutorial to understand - example from https://docs.python.org/2/howto/argparse.html - the program name is followed by the input to the argument

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",
                    type=int)
args = parser.parse_args()
print (args.square**2)
