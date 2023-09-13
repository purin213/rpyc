import rpyc
import conn = rpyc.classic.connect("localhost")
conn.execute("print('Hi mom')")
conn.execute('import math')
conn.eval('2*math.pi')
