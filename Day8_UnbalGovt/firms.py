'''
------------------------------------------------------------------------
This module contains the functions that generate the variables
associated with firms' optimization in the steady-state or in the
transition path of the overlapping generations model with S-period lived
agents and endogenous labor supply from Chapter 7 of the OG textbook.

This Python module imports the following module(s): None

This Python module defines the following function(s):
    get_w()
    get_r()
------------------------------------------------------------------------
'''
# Import packages

'''
------------------------------------------------------------------------
    Functions
------------------------------------------------------------------------
'''


def get_w(params, K, L):
    '''
    --------------------------------------------------------------------
    Solve for steady-state wage w or time path of wages w_t
    --------------------------------------------------------------------
    INPUTS:
    params = length 2 tuple, (A, alpha)
    A      = scalar > 0, total factor productivity
    alpha  = scalar in (0, 1), capital share of income
    K      = scalar > 0 or (T+S-2,) vector, steady-state aggregate
             capital stock or time path of the aggregate capital stock
    L      = scalar > 0 or (T+S-2,) vector, steady-state aggregate
             labor or time path of aggregate labor

    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None

    OBJECTS CREATED WITHIN FUNCTION:
    w = scalar > 0 or (T+S-2) vector, steady-state wage or time path of
        wage

    FILES CREATED BY THIS FUNCTION: None

    RETURNS: w
    --------------------------------------------------------------------
    '''
    A, alpha = params
    w = (1 - alpha) * A * ((K / L) ** alpha)

    return w


def get_r(params, K, L):
    '''
    --------------------------------------------------------------------
    Solve for steady-state interest rate r or time path of interest
    rates r_t
    --------------------------------------------------------------------
    INPUTS:
    params = length 4 tuple, (A, alpha, delta, tau_c)
    A      = scalar > 0, total factor productivity
    alpha  = scalar in (0, 1), capital share of income
    delta  = scalar in (0, 1), per period depreciation rate
    tau_c  = scalar, corporate income tax rate
    K      = scalar > 0 or (T+S-2,) vector, steady-state aggregate
             capital stock or time path of the aggregate capital stock
    L      = scalar > 0 or (T+S-2,) vector, steady-state aggregate
             labor or time path of aggregate labor

    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None

    OBJECTS CREATED WITHIN FUNCTION:
    r = scalar > 0 or (T+S-2) vector, steady-state interest rate or time
        path of interest rate

    FILES CREATED BY THIS FUNCTION: None

    RETURNS: r
    --------------------------------------------------------------------
    '''
    A, alpha, delta, tau_c = params
    r = (1-tau_c)*(alpha * A * ((L / K) ** (1 - alpha)) - delta)

    return r
