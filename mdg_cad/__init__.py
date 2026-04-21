'''
just some simple functions that help me with cad, design, and machining
'''
from math import *
from IPython import embed

def in2mm(in_val):
    mm_val = in_val*25.4
    return mm_val

def mm2in(mm_val):
    in_val = mm_val/25.4
    return in_val

def midp(a,b):
    return 0.5*(a+b)

def frac(value,denom=32):
    '''
    this returns the two closest fractional values to an input value, 
    unless the value is equal to a fraction in which case it returns one value. 
    denom = largest denominator. All denominators are some factor of this. 
    '''
    product = value*denom
    if product%1 == 0:
        reduce = reduce_fraction(int(product),int(denom))
        return (f"({value}) is equal to {reduce[0]}/{reduce[1]} ({reduce[0]/reduce[1]})",)
    else:
        upper_frac = reduce_fraction(ceil(product),denom)
        lower_frac = reduce_fraction(floor(product),denom)
        return (f"({value}) is between {lower_frac[0]}/{lower_frac[1]} ({lower_frac[0]/lower_frac[1]}) and {upper_frac[0]}/{upper_frac[1]} ({upper_frac[0]/upper_frac[1]})")
    
def fracmm(value,denom=32):
    '''
    this is the same as frac(), but takes a millimeter value and returns a pair of fractional inch values.
    '''
    inch_val = mm2in(value)
    return frac(inch_val,denom=denom)
    

def reduce_fraction(num,denom):
    '''
    reduces a fraction. num and denom must be whole numbers
    '''
    #find greatest commmon factor
    num_factors = [i for i in range(1, num + 1) if num % i == 0]
    denom_factors = [i for i in range(1, denom + 1) if denom % i == 0]
    gcf = max(set(num_factors) & set(denom_factors))

    #return reduced fraction
    return (int(num/gcf),int(denom/gcf))


# ******************* #
# Machining functions #
# ******************* #

def sfm2rpm(sfm,D,D_unit = 'mm'):
    
    if D_unit == 'mm':
        rpm = sfm*(304.8/(pi*D))
    elif D_unit == 'in':
        rpm = sfm*(12/(pi*D))
    return rpm




# embed()

