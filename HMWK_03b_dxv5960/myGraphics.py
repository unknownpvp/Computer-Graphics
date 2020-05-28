# Danny Vu
# dxv5960
# 2019-04-11

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

  def create_graphic_objects( self, canvas, modelData, doClip ) :
    
    ( xMin, yMin, xMax, yMax ) = modelData.getViewport()
    limits = ( xMin, yMin, xMax, yMax )

    if ( doClip ) :
      for v1Num, v2Num, v3Num in modelData.getFaces() :
        x1, y1, _ = modelData.getTransformedVertex( v1Num )
        x2, y2, _ = modelData.getTransformedVertex( v2Num )
        x3, y3, _ = modelData.getTransformedVertex( v3Num )

        ( doDraw, _x1, _y1, _x2, _y2 ) = clipLine( x1, y1, x2, y2, limits )
        ( doDraw, _x2, _y2, _x3, _y3 ) = clipLine( x2, y2, x3, y3, limits )
        ( doDraw, _x3, _y3, _x1, _y1 ) = clipLine( x3, y3, x1, y1, limits )
   
        if ( doDraw ) :
          canvas.create_line( _x1, _y1, _x2, _y2, _x3, _y3, _x1, _y1 )
        else :
          canvas.create_line( x1, y1, x2, y2, x3, y3, x1, y1 )

    else :
      for v1Num, v2Num, v3Num in modelData.getFaces() :
        x1, y1, _ = modelData.getTransformedVertex( v1Num )
        x2, y2, _ = modelData.getTransformedVertex( v2Num )
        x3, y3, _ = modelData.getTransformedVertex( v3Num )

        canvas.create_line( x1, y1, x2, y2, x3, y3, x1, y1 )

  def redisplay( self, canvas, event ) :
    pass

#----------------------------------------------------------------------
