import sys
from ROOT import gSystem
gSystem.Load("libppSRC_ppSRCpackage")
from ROOT import sample

try:

    print "PyROOT recognized your class %s" % str(sample)

except NameError:

    print "Failed importing ppSRCpackage..."

sys.exit(0)

