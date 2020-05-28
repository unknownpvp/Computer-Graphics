# Vu, Danny
# dxv5960
# 2019-04-23

#----------------------------------------------------------------------
# This code was originally created by Prof. Farhad Kamangar.
# It has been significantly modified and updated by Brian A. Dalio for
# use in CSE 4303 / CSE 5365 in the 2018 Fall semester.

#----------------------------------------------------------------------
from CohenSutherland import clipLine
from bezier import resolveBezierPatch

class cl_world :
  def __init__( self, objects = [], canvases = [] ) :
    self.objects = objects
    self.canvases = canvases

  def add_canvas( self, canvas ) :
    self.canvases.append( canvas )
    canvas.world = self

  def reset( self ) :
    self.objects = []
    for canvas in self.canvases :
      canvas.delete( 'all' )

  def create_graphic_objects( self, canvas, modelData, doClip, doPerspective, doEuler, resolution ) :
    
    width  = int( canvas.cget( "width" ) )
    height = int( canvas.cget( "height" ) )
    v = modelData.getViewport()
    vxMin = v[0] * width
    vxMax = v[2] * width
    vyMin = v[1] * height
    vyMax = v[3] * height
    portal = ( vxMin, vyMin, vxMax, vyMax )

    for v1Num, v2Num, v3Num in modelData.getFaces() :
        x1, y1, _ = modelData.getTransformedVertex( v1Num, doPerspective, doEuler )
        x2, y2, _ = modelData.getTransformedVertex( v2Num, doPerspective, doEuler )
        x3, y3, _ = modelData.getTransformedVertex( v3Num, doPerspective, doEuler )

        canvas.create_line( x1, y1, x2, y2, x3, y3, x1, y1 )

    controlPts = []
    for p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16 in modelData.getPatches() :
      cp1 = modelData.getTransformedVertex( p1, doPerspective, doEuler )
      cp2 = modelData.getTransformedVertex( p2, doPerspective, doEuler )
      cp3 = modelData.getTransformedVertex( p3, doPerspective, doEuler )
      cp4 = modelData.getTransformedVertex( p4, doPerspective, doEuler )
      cp5 = modelData.getTransformedVertex( p5, doPerspective, doEuler )
      cp6 = modelData.getTransformedVertex( p6, doPerspective, doEuler )
      cp7 = modelData.getTransformedVertex( p7, doPerspective, doEuler )
      cp8 = modelData.getTransformedVertex( p8, doPerspective, doEuler )
      cp9 = modelData.getTransformedVertex( p9, doPerspective, doEuler )
      cp10 = modelData.getTransformedVertex( p10, doPerspective, doEuler )
      cp11 = modelData.getTransformedVertex( p11, doPerspective, doEuler )
      cp12 = modelData.getTransformedVertex( p12, doPerspective, doEuler )
      cp13 = modelData.getTransformedVertex( p13, doPerspective, doEuler )
      cp14 = modelData.getTransformedVertex( p14, doPerspective, doEuler )
      cp15 = modelData.getTransformedVertex( p15, doPerspective, doEuler )
      cp16 = modelData.getTransformedVertex( p16, doPerspective, doEuler )
        
      controlPts = ( cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8, cp9, cp10, cp11, cp12, cp13, cp14, cp15, cp16 )
      pointList = resolveBezierPatch( resolution, controlPts )

      for row in range( 0, resolution-2 ) :
        rowStart = row * resolution

        for col in range( 0, resolution-2 ) :
          here = rowStart + col
          there = here + resolution

          triangleA = ( pointList[here], pointList[there], pointList[there+1] )
          triangleB = ( pointList[there+1], pointList[here+1], pointList[here] )

          drawTriangle( canvas, v1, v2, v3, portal, doClip )
        

    if ( doClip ) :
      for v1Num, v2Num, v3Num in modelData.getFaces() :
        v1 = modelData.getTransformedVertex( v1Num, doPerspective, doEuler )
        v2 = modelData.getTransformedVertex( v2Num, doPerspective, doEuler )
        v3 = modelData.getTransformedVertex( v3Num, doPerspective, doEuler )

        for (vax, vay, _),(vbx, vby, _) in [(v1,v2),(v2,v3),(v3,v1)] :
            ( doDraw, vax, vay, vbx, vby ) = clipLine( vax, vay, vbx, vby, portal )
           
            if ( doDraw ) :
              canvas.create_line( vax, vay, vbx, vby )

    else :
      for v1Num, v2Num, v3Num in modelData.getFaces() :
        x1, y1, _ = modelData.getTransformedVertex( v1Num, doPerspective, doEuler )
        x2, y2, _ = modelData.getTransformedVertex( v2Num, doPerspective, doEuler )
        x3, y3, _ = modelData.getTransformedVertex( v3Num, doPerspective, doEuler )

        canvas.create_line( x1, y1, x2, y2, x3, y3, x1, y1 )

  def redisplay( self, canvas, event ) :
    pass

  def drawTriangle( canvas, v1, v2, v3, portal, doClip ) :
    for v1Num, v2Num, v3Num in modelData.getFaces() :
        v1 = modelData.getTransformedVertex( v1Num, doPerspective, doEuler )
        v2 = modelData.getTransformedVertex( v2Num, doPerspective, doEuler )
        v3 = modelData.getTransformedVertex( v3Num, doPerspective, doEuler )
        
        for (vax, vay, _),(vbx, vby, _) in [(v1,v2),(v2,v3),(v3,v1)] :
            ( doDraw, vax, vay, vbx, vby ) = clipLine( vax, vay, vbx, vby, portal )
           
            if ( doDraw ) :
              canvas.create_line( vax, vay, vbx, vby )
    

#----------------------------------------------------------------------
