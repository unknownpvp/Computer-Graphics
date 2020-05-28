# Vu, Danny
# dxv5960
# 2019-04-23

#----------------------------------------------------------------------
# This code was originally created by Prof. Farhad Kamangar.
# It has been significantly modified and updated by Brian A. Dalio for
# use in CSE 4303 / CSE 5365 in the 2018 Fall semester.

#----------------------------------------------------------------------
from CohenSutherland import clipLine

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

  def create_graphic_objects( self, canvas, modelData, doClip, doPerspective, doEuler ) :
    
    width  = int( canvas.cget( "width" ) )
    height = int( canvas.cget( "height" ) )
    v = modelData.getViewport()
    vxMin = v[0] * width
    vxMax = v[2] * width
    vyMin = v[1] * height
    vyMax = v[3] * height
    portal = ( vxMin, vyMin, vxMax, vyMax )

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

#----------------------------------------------------------------------
