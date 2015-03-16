import conversions
import unittest


class CelctoFarKnown(unittest.TestCase):
	knownvalues = ( (0,32),(5,41),(7,44.6),(13,55.4),(16,60.8),(26,78.8),(29,84.2),(37,98.6),(52,125.6),(100,212),(138,280.4),(142,287.6),(145,293),(210,410))
	
	def testToFarKnownValues(self):
		for celc, far in self.knownvalues:
			result = conversions.convertCelciustoFahrenheit(celc)
			self.assertEqual(far, result)
	
class CelctoFarBadInput(unittest.TestCase):
	def testNonNumeric(self):
		badinputs = ["Text String", ("Text","Tuple"), ["Text", "List"],True,False,None]
		for member in badinputs:
			self.assertRaises(conversions.NonNumericInputError, conversions.convertCelciustoFahrenheit, member)
	
	def testLowerLimit(self):
		self.assertRaises(conversions.LowerLimitError, conversions.convertCelciustoFahrenheit, -300)
		

class CelctoKelvinKnown(unittest.TestCase):
	knownvalues = ( (-273.15, 0), (-260,13.15), (-200,73.15), (-160, 113.15), (-100, 173.15), (0,273.15),(50,323.15),(100,373.15),(200,473.15),(250,523.15),(300,573.15))
	def testToKelvinKnownValues(self):
		for celc, kelv in self.knownvalues:
			result = conversions.convertCelsiustoKelvin(celc)
			self.assertEqual(kelv, result)

class CelctoKelvinBadInput(unittest.TestCase):
	def testNonNumeric(self):
		badinputs = ["Text String", ("Text","Tuple"), ["Text", "List"],True,False,None]
		for member in badinputs:
			self.assertRaises(conversions.NonNumericInputError, conversions.convertCelsiustoKelvin, member)
			
	def testLowerLimit(self):
		self.assertRaises(conversions.LowerLimitError, conversions.convertCelsiustoKelvin, -1)
	
if __name__ == '__main__':
    unittest.main()
			
	













		