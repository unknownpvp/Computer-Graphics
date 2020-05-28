import numpy

def resolveBezierPatch( resolution, controlPts ) :
    pointList = []
    coeffs = []
    for u in numpy.linspace( 0.0, 1.0, resolution ) :
        for v in numpy.linspace( 0.0, 1.0, resolution ) :
            point = ( 0.0, 0.0, 0.0 )
            for i in range( 4 ) :
                for j in range( 4 ):
                    coeffs = compute(i,j)
                    point = point + coeffs * controlPts
                


            pointList.append( point )


    return pointList

def compute( u, v ) :
    c00 = (-u+1)**3 * (-v+1)**3
    c02 = 3*v**2 * (-u+1)**3 * (-v+1)
    
    c10 = 3*u * (-u+1)**2 * (-v+1)**3
    c12 = 9*u*v**2 * (-u+1)**2 * (-v+1)

    c20 = 3*u**2 * (-u+1) * (-v+1)**3
    c22 = 9*u**2*v**2 * (-u+1) * (-v+1)

    c30 = u**3 * (-v+1)**3
    c32 = 3*u**3*v**2 * (-v+1)

    c01 = 3*v * (-u+1)**3 * (-v+1)**2
    c03 = v**3 * (-u+1)**3
  
    c11 = 9*u*v * (-u+1)**2 * (-v+1)**2
    c13 = 3*u*v**3 * (-u+1)**2

    c21 = 9*u**2*v * (-u+1) * (-v+1)**2
    c23 = 3*u**2*v**3 * (-u+1)
  
    c31 = 3*u**3*v * (-v+1)**2
    c33 = u**3 * v**3

    return c00

    
