# Vu, Danny
# dxv5960
# 2019-04-04

#----------------------------------------------------------------------
# This code was originally created by Prof. Farhad Kamangar.
# It has been significantly modified and updated by Brian A. Dalio for
# use in CSE 4303 / CSE 5365 in the 2019 Spring semester.

#----------------------------------------------------------------------
class cl_world :
  def __init__( self, objects = [], canvases = [] ) :
    self.canvases = canvases

  def add_canvas( self, canvas ) :
    self.canvases.append( canvas )
    canvas.world = self

  def reset( self ) :
    for canvas in self.canvases :
      canvas.delete( 'all' )

  def create_graphic_objects( self, canvas, model ) :
    result = model.getFaces()
    vertices = model.getVertices()
    v1 = model.getTransformedVertex(vertices)
    (x1,y1) = vertices[v1]
    canvas.create_line(x1,y1,x2,y2)
    canvas.create_line(x2,y2,x3,y3)
    canvas.create_line(x3,y3,x1,y1)
    

#----------------------------------------------------------------------
