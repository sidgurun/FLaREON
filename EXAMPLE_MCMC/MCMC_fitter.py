import sys 

import numpy as np

import FLaREON as Lya 

import emcee

#==============================================================================#
#==============================================================================#
#==============================================================================#

# In this example we ilustrate how FLaREON can be wrap up with emcee. 

# In sort, we are going to generate a line profile using FLaREON (and a given gas geometry) and then we will fit it with another out flow geometry.

# This example only ilustrates how to make the wrap up. If you want to fit a lyman alpha line of yours you should change the code acordingly.

# This is not a emcee tutorial. You should consider understanding how emcee works before looking at this example.

#==============================================================================#
#==============================================================================#
#==============================================================================#

# First lets generate the line profile we want to fit.

# We need to set the ourflow properties :

V_exp_Prob =  55.     # Expansion velocity in km/s
logNH_Prob =  17.625  # log Column density ( cm ** -2 )
logta_Prob =  -0.234  # tau_a

# Now we set the outflow gemetry we want to use.

Geometry_Prob = 'Thin_Shell' 

# We define the array of wavelengths 

wave_Arr_Prob = np.linspace( 1215.68 - 20 , 1215.68+20 , 1000 ) * 1e-10 # in meters!

# We load once FLaREON grid containing the line profile information.

DATA_FLaREON_Prob = Lya.load_Grid_Line( Geometry_Prob )  

# We generate our 'problem line'

Line_Prob_Arr = Lya.RT_Line_Profile_MCMC( Geometry_Prob , wave_Arr_Prob , V_exp_Prob , logNH_Prob , 10**logta_Prob , DATA_FLaREON_Prob )

#==============================================================================#
#==============================================================================#
#==============================================================================#

# Now we define some usefull fucntions to the MCMC

#==============================================================================#
def KS_stimator( Dist1  , Dist2 ):

    '''
        This functions computes the Kolmogorov-Smirnov estimator for 2 distributions Dist1 and Dist2 evaluated in the same array. In our case, the same wavelenght
    '''

    Dist1 = np.absolute( Dist1 * 1. / np.trapz( Dist1 ) )
    Dist2 = np.absolute( Dist2 * 1. / np.trapz( Dist2 ) )

    Cum_1 = np.zeros( len(Dist1) )
    Cum_2 = np.zeros( len(Dist2) )

    Cum_1[0] = Dist1[0] 
    Cum_2[0] = Dist2[0] 

    for i in range( 1 , len(Dist1) ):

        Cum_1[i] = Cum_1[i-1] + Dist1[i] 
        Cum_2[i] = Cum_2[i-1] + Dist2[i] 

    KS = np.amax( np.absolute( Cum_1 - Cum_2 ) )

    return KS
#==============================================================================#
def Grid_Boundaries( P ):

	'''
		This function check if the walker is inside the FlaREON Grid.

        If for some reason you wish to restric the paramter range you can do it here. Just change the numbers.
	'''

	V_exp_mcmc = P[0]
	logNH_mcmc = P[1]
	logta_mcmc = P[2]

	if V_exp_mcmc < 10.0   or V_exp_mcmc >= 1000   : return False
	if logNH_mcmc < 17.0   or logNH_mcmc >= 22.0   : return False
	if logta_mcmc < -3.75  or logta_mcmc >= -0.125 : return False

	return True
#==============================================================================#
#==============================================================================#
def lnprob( P , Geometry , wave_Arr , Line_Prob_Arr , DATA_FLaREON ):

    '''
        This is the main function in the MCMC run. It takes the coordenates of a walker in the V_exp - N_H - tau_a space and return how likely are the Problem line and the Walker line.
    '''

	# First we check that the walker is in the grid. If false we tell emcee that the walker is lost.

    if not Grid_Boundaries( P ):
        return -np.inf

    V_exp_mcmc = P[0]
    logNH_mcmc = P[1]
    logta_mcmc = P[2]

    # We compute the line in the Walker position. 

    Line_mcmc_Arr = Lya.RT_Line_Profile_MCMC( Geometry , wave_Arr , V_exp_mcmc , logNH_mcmc , 10**logta_mcmc , DATA_FLaREON )

    # We compute the Kolmogorov-Smirnov estimator between the problem line and the walker line. 

    KS = KS_stimator( Line_mcmc_Arr , Line_Prob_Arr )

    # We return the quantity that we want to optimize. You might want to change this depending on you individual problem. 

    return - ( KS * 1e6 )**4 
#==============================================================================#
#==============================================================================#
#==============================================================================#

# We define the main funcion that joins all together.

def MCMC_code( Geometry_mcmc , wavelength_Arr_Prob , Line_Prob , Ndim , Nsteps , Nwalkwer , INSIDE_BICONE=None ):

    '''
        This function takes a line profile that we want to fit, the geometry that we want to use to fit the line and the MCMC configuration parameters.

        Ndim    is the number of dimensions that we are exploring. In these example Ndim = 3 since we wander in the V_exp-N_H-tau_a space.

        Nsteps  is the number of iterations in the MCMC algorithm for each walker.

        Nwalker is the number of walkers trying to find the best location.

        Then, while running the MCMC it writes a file with the walker positions and performance.

        We will analize the mcmc output later. Using another code.
    '''

    # First we load the FLaREON grids for the wished geometry 

    DATA_FLaREON_MCMC = Lya.load_Grid_Line( Geometry_mcmc , INSIDE_BICONE=INSIDE_BICONE )

    # We define the region where we will throw the walkers.

    V_exp_in = [ 10.0  , 1000.    ]
    logNH_in = [ 17.0  ,   22.    ]
    logta_in = [ -3.75 ,   -0.125 ]
    
    p0 = np.zeros( Ndim * Nwalkwer ).reshape( Nwalkwer , Ndim )
    
    p0[:,0] = np.random.rand( Nwalkwer ) * (   V_exp_in[1] -   V_exp_in[0] ) +   V_exp_in[0]
    p0[:,1] = np.random.rand( Nwalkwer ) * (   logNH_in[1] -   logNH_in[0] ) +   logNH_in[0]
    p0[:,2] = np.random.rand( Nwalkwer ) * (   logta_in[1] -   logta_in[0] ) +   logta_in[0]
    
    # We build the emcee Sampler.
    
    sampler = emcee.EnsembleSampler( Nwalkwer , Ndim , lnprob , args=[ Geometry_mcmc , wavelength_Arr_Prob , Line_Prob , DATA_FLaREON_MCMC ] )

    # We define the name where the output is writen.     
    
    name_file = 'mcmc_output_' + Geometry_mcmc + '_' + str(INSIDE_BICONE) + '_ndim_' + str(Ndim) + '_nsteps_' + str(Nsteps) + '_nwalkers_' + str(Nwalkwer) + '.txt'
    
    f = open(name_file,'w')
    f.close()
   
    # We starts running the MCMC
 
    print 'The MCMC is... running!'

    ccc = 10

    paso = 0
    for result in sampler.sample( p0 , iterations=Nsteps , storechain=False ):
        position = result[0]
        prob     = result[1]
    
        f = open(name_file, 'a')
    
        for k in range(position.shape[0]):
    
            line = '%E %E ' % ( k , paso , )
    
            for coor in position[k]:
    
                line += '%E ' % (coor)
    
            line += '%E\n' % (prob[k],)
    
            f.write(line)
        paso +=1
   
        if paso *100. / Nsteps >= ccc: 
            print ccc , '%'
            ccc += 10
    
        f.close()
    
    return 
#==============================================================================#
#==============================================================================#
#==============================================================================#

# This part of the code exacute the previous define functions. 

# We set the MCMC parameters:
Ndim = 3
Nsteps = 1000
Nwalkwer = 100

# We define the outflow geometry that we want to use to fit the problem line profile
Geo_to_fit = 'Galactic_Wind'

# We pass the function all the necesart variables, including the problem line profile

MCMC_code( Geo_to_fit , wave_Arr_Prob , Line_Prob_Arr , Ndim , Nsteps , Nwalkwer , INSIDE_BICONE=None )
 

print 'Done! You should have a new file with the mcmc chains!'

