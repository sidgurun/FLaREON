import sys

import numpy as np


import corner

# mcmc_output_Thin_Shell_None_ndim_3_nsteps_100_nwalkers_20.txt

file_name = sys.argv[1]


######################################################################
######################################################################
def stract_properties( file_name ):

    Geo = file_name.split('_')[2]

    if Geo == 'Bicone'   : Geometry = 'Bicone_X_Slab' 
    if Geo == 'Galactic' : Geometry = 'Galactic_Wind' 
    if Geo == 'Thin'     : Geometry = 'Thin_Shell' 

    ll = len( Geometry.split('_') )

    Ndim     = int( file_name.split('_')[ 4 + ll ] )

    Nsteps   = int( file_name.split('_')[ 6 + ll ] )

    Nwalkers = int( file_name.split('_')[ 8 + ll ].split('.')[0] )

    
    prop={}

    prop[ 'Geometry' ] = Geometry

    prop[ 'Ndim'     ] = Ndim
    prop[ 'Nsteps'   ] = Nsteps
    prop[ 'Nwalkers' ] = Nwalkers

    return prop
######################################################################
######################################################################

prop = stract_properties( file_name )

Ndim     = prop[ 'Ndim'     ]
Nsteps   = prop[ 'Nsteps'   ]
Nwalkers = prop[ 'Nwalkers' ]

data = np.loadtxt( file_name )

chains = np.zeros( Nsteps * Nwalkers * ( Ndim + 1 ) ).reshape( Nwalkers , Nsteps , ( Ndim + 1 ) )

Good_thresshold = 1e99

good_chains = []

for j in range( 0 , Nwalkers ) :

        _chain = data[ data[ : , 0] == j ] 

        chains[ j  , : , 0 ] =   _chain[ : , 2 ] # Vel
        chains[ j  , : , 1 ] =   _chain[ : , 3 ] # logNH
        chains[ j  , : , 2 ] =   _chain[ : , 4 ] # logta
        chains[ j  , : , 3 ] = - _chain[ : , 5 ] # -xi

        if np.median( chains[ j , 800: , 3 ] ) < Good_thresshold : good_chains.append( j )


PLOT_CHAINS = False
if PLOT_CHAINS : 
    for j in range( 0 , Nwalkers ) :
    
        _chain = chains[ j , : , 3 ]
    
        semilogy( np.arange( 0 , len( _chain ) ) , _chain , 'k' , alpha=0.2 )
   
        title( prop['Geometry'] , size=20 )
 
    show()


SUPER_CHANGES = np.zeros( Nsteps * len(good_chains) * ( Ndim + 1 ) ).reshape( len(good_chains) , Nsteps , ( Ndim + 1 ) )

#print SUPER_CHANGES.shape

cc=0
for j in good_chains:

    SUPER_CHANGES[ cc ] = chains[ j ] 

    cc += 1 

SUPER_CHANGES = SUPER_CHANGES[ : , 800: ]

Vexp_Q50 = np.percentile( SUPER_CHANGES[:,:,0 ] , 50 )
Vexp_Q32 = np.percentile( SUPER_CHANGES[:,:,0 ] , 32 )
Vexp_Q68 = np.percentile( SUPER_CHANGES[:,:,0 ] , 68 )

logNH_Q50 = np.percentile( SUPER_CHANGES[:,:,1 ] , 50 )
logNH_Q32 = np.percentile( SUPER_CHANGES[:,:,1 ] , 32 )
logNH_Q68 = np.percentile( SUPER_CHANGES[:,:,1 ] , 68 )

logta_Q50 = np.percentile( SUPER_CHANGES[:,:,2 ] , 50 )
logta_Q32 = np.percentile( SUPER_CHANGES[:,:,2 ] , 32 )
logta_Q68 = np.percentile( SUPER_CHANGES[:,:,2 ] , 68 )


print 'if the ouflow geometry is ' + prop['Geometry'] + ', then, the best fitting values are...:'

print '    V_exp         = ' , Vexp_Q50  
#print '    V_exp_err_top = ' , Vexp_Q68 -  Vexp_Q50  
#print '    V_exp_err_bot = ' , Vexp_Q50 -  Vexp_Q32 
print '    logNH         = ' , logNH_Q50 
#print '    logNH_err_top = ' , logNH_Q68 - logNH_Q50 
#print '    logNH_err_bot = ' , logNH_Q50 - logNH_Q32 
print '    logta         = ' , logta_Q50
#print '    logta_err_top = ' , logta_Q68 - logta_Q50 
#print '    logta_err_bot = ' , logta_Q50 - logta_Q32 , '\n'

PLOT_STEPS = False
if PLOT_STEPS :
    coor = np.zeros( len( good_chains ) * Nsteps * Ndim ).reshape( len( good_chains ) * Nsteps , Ndim )
    
    cc = 0
    
    for i in range( 0 , len( data ) ) :
    
        if data[i][0] in good_chains :
    
            coor[ cc ] = data[ i ,  2:-1 ]
    
            cc += 1 
    
    fig = corner.corner( coor )# , labels = torder, truths = trues)
    #fig = corner.corner(samples , labels = torder, truths = trues)
    
    show()



