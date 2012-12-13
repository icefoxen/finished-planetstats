# Simple program to output/graph the pressure of a planet given inputs:
# Density, gravity and radius.
# Wrong, but sort of gives an idea.

def pressureAtDepth(rho, g, d):
   return (rho * g) * d

def planetPressure(rho, g, r, increments):
   accm = []
   step = r / increments
   for d in range(0, r, step):
      accm.append(Gpa(pressureAtDepth(rho, g, d)))
   return accm

def Gpa(pascals):
   return pascals / 1000000000.0

def mercuryPressure(increments):
   return planetPressure(5400, 3.7, 2439000, increments)

def venusPressure(increments):
   return planetPressure(5200, 8.9, 6051000, increments)

def earthPressure(increments):
   return planetPressure(5500, 9.8, 6371000, increments)

def moonPressure(increments):
   return planetPressure(3300, 1.6, 1737000, increments)

def marsPressure(increments):
   return planetPressure(3900, 3.7, 3386000, increments)

def ioPressure(increments):
   return planetPressure(3500, 1.8, 1821000, increments)
 
def europaPressure(increments):
   return planetPressure(3000, 1.3, 1593000, increments)


# Run as a simple script if called as a script.
if __name__ == '__main__':
   print( "Mercury:" )
   print( mercuryPressure(10) )
   print( "Venus:" )
   print( venusPressure(10) )
   print( "Earth:" )
   print( earthPressure(10) )
   print( "Moon:" )
   print( moonPressure(10) )
   print( "Mars:" )
   print( marsPressure(10) )
   print( "Io:" )
   print( ioPressure(10) )
   print( "Europa:" )
   print( europaPressure(10) )
