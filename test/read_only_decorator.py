from read_only_class_attributed import read_only

#example for all read only attributes
@read_only('*')
class _CONSTANTS:
    pi = 3.14159
    G = 6.67430e-11

CONSTANTS = _CONSTANTS()


#example for some read only attributes
@read_only('pi', 'G')
class _PLANETCONSTANTS:
    pi = 3.14159
    G = 6.67430e-11
    g = 9.18 #can change
    planet = 'Earth' #can change

PLANETCONSTANTS = _PLANETCONSTANTS()

def modifyAttr():
    CONSTANTS.pi = 2

def modifySelectedAttr():
    PLANETCONSTANTS.G = 5

class ReadonlyTestCase(unittest.TestCase):
    def testErrorOnModifying(self):
        self.assertRaises(AttributeError, modifyAttr)
    
    def testErrorOnModifyingSelected(self):
        self.assertRaises(AttributeError, modifySelectedAttr)
    
    def testNoErrorOnReading(self):
        try:
            mypi = CONSTANTS.pi
        except:
            self.fail("Reading read only attributes should not throw exceptions")
