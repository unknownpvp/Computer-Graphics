# Vu, Danny
# dxv5960
# 2019-02-06

import sys

class ModelData() :
  def __init__( self, inputFile = None ) :
    self.m_Vertices = []
    self.m_Faces    = []
    
    if inputFile is not None :
      # File name was given.  Read the data from the file.
      self.loadFile( inputFile )

  def loadFile( self, inputFile ) :
    ##################################################
    # Put your Python code for reading and processing the lines
    # from the source file in the place of the comments below.
    # (The comments give all the direction you should need to
    #  write the code.  It's not all that difficult.)
    ##################################################
    with open( inputFile, 'r' ) as fp :
          lines = fp.read().replace('\r', '' ).split( '\n' )
    # Read each line of the file.
    for ( index, line ) in enumerate( lines, start = 1 ) :
          line = line.strip()
    # Ignore any blank line (or line that's only whitespace characters).
          if line.strip():  
    # Ignore any line that starts with a #.
                if not line.strip().startswith("#"):
    # For the remaining lines, if the line starts with:
    #  f -- Append the three integers as a tuple to self.m_Faces.
    #  v -- Append the three floats as a tuple to self.m_Vertices.
                    if(line[0]=='v'):
                        try:
                            (_,x,y,z)=line.split()
                            x = float(x)
                            y = float(y)
                            z = float(z)
                        except:
                            print('Line {} ''{}'' is unrecognized.'.format('index','line'))
                    if(line[0]=='f'):
                        try:
                            (_,x,y,z)=line.split()
                            x = int(x)-1
                            y = int(y)-1
                            z = int(z)-1
                        except:
                            print('Line {} ''{}'' is unrecognized.'.format('index','line'))
    # Note that the above comments mention integers and floats.
    # You must convert the string representation of the integers
    # and floats into actual numbers.  There may be formatting
    # errors in the file, so ensure you catch (and report)
    # conversion errors.
                    
    # It is an error if a line starts with any other character.
    # Print an error message for that line, but keep going and look
    # at the rest of the lines.
    
    # A model file may have any number of f and v lines.  In fact,
    # some model files we will use will have thousands of v and f
    # lines.

    ##################################################
    # All the code you have to write should go above here in the
    # body of the loadFile() routine.
    ##################################################

  def getFaces( self )    : return self.m_Faces
  def getVertices( self ) : return self.m_Vertices

#---------#---------#---------#---------#---------#--------#
def _main() :
  # Get the file name to load.
  fName = sys.argv[1]

  # Create a ModelData object to hold the model data from
  # the supplied file name.
  model = ModelData( fName )

  # Now that it's loaded, print out a few statistics about
  # the model data that we just loaded.
  print( f'{fName}: {len( model.getVertices() )} vert%s, {len( model.getFaces() )} face%s' % (
    'ex' if len( model.getVertices() ) == 1 else 'ices',
    '' if len( model.getFaces() ) == 1 else 's' ))

  print( 'First 3 vertices:' )
  for v in model.getVertices()[0:3] :
    print( f'     {v}' )

  print( 'First 3 faces:' )
  for f in model.getFaces()[0:3] :
    print( f'     {f}' )

#---------#
if __name__ == '__main__' :
  _main()

#---------#---------#---------#---------#---------#--------#
