import conversions_refactored
import unittest



class CelctoFarKnown(unittest.TestCase):
	knownvalues = ( (0,32),(7,44.6),(13,55.4),(16,60.8),(26,78.8),(29,84.2),(37,98.6),(52,125.6),(100,212),(138,280.4),(142,287.6),(145,293),(210,410))
	
	def testToFarKnownValues(self):
		"""CelctoFar should succeed for all known inputs"""
		for celc, far in self.knownvalues:
			result = conversions_refactored.convert("celcius","fahrenheit",celc)
			self.assertEqual(far, result)
	
class CelctoFarBadInput(unittest.TestCase):
	fromUnit = "celcius"
	toUnit = "fahrenheit"
	def testNonNumeric(self):
		"""CelctoFar should fail with non-numeric input"""
		badinputs = ["Text String", ("Text","Tuple"), ["Text", "List"],True,False,None]
		for Value in badinputs:
			self.assertRaises(conversions_refactored.NonNumericInputError, conversions_refactored.convert, self.fromUnit,self.toUnit,Value)

	def testLowerLimit(self):
		"""Celftofar should fail on input less than absolute zero"""
		self.assertRaises(conversions_refactored.LowerLimitError, conversions_refactored.convert, self.fromUnit,self.toUnit,-300)
		
class CelctoKelvinKnown(unittest.TestCase):
	fromUnit = "celcius"
	toUnit = "kelvin"
	knownvalues = ( (-273.15, 0), (-260,13.15), (-200,73.15), (-160, 113.15), (-100, 173.15), (0,273.15),(50,323.15),(100,373.15),(200,473.15),(250,523.15),(300,573.15))
	def testToKelvinKnownValues(self):
		"""CelctoKelvin should succeed on all known inputs"""
		for celc, kelv in self.knownvalues:
			result = conversions_refactored.convert(self.fromUnit,self.toUnit,celc)
			self.assertEqual(kelv, result)

class CelctoKelvinBadInput(unittest.TestCase):
	fromUnit = "celcius"
	toUnit = "kelvin"
	def testNonNumeric(self):
		"""CelctoKelvin should fail on non-numeric input"""
		badinputs = ["Text String", ("Text","Tuple"), ["Text", "List"],True,False,None]
		for Value in badinputs:
			self.assertRaises(conversions_refactored.NonNumericInputError, conversions_refactored.convert,self.fromUnit,self.toUnit, Value)
			
	def testLowerLimit(self):
		"""CelctoKelvin should fail on input less than absolute zero"""
		self.assertRaises(conversions_refactored.LowerLimitError, conversions_refactored.convert,self.fromUnit,self.toUnit, -300)
	
class FahrenheittoCelciusKnown(unittest.TestCase):
	fromUnit = "fahrenheit"
	toUnit = "celcius"
	knownvalues = ((-459.67,-273.15),(-292.00,-180.00), (-94.00, -70.00), (-4.00, -20.00), (32.00, 0.00), (86.00, 30.00), (176.00, 80.00),(284.00,140.00), (572.00, 300))
	def testFahrenheittoCelciusValues(self):
		"""CelctoKelvin should succeed on all known inputs"""
		for input, output in self.knownvalues:
			result = conversions_refactored.convert(self.fromUnit, self.toUnit, input)
			self.assertEqual(result, output)
		
class FahrenheittoCelciusBadInput(unittest.TestCase):
	fromUnit = "fahrenheit"
	toUnit = "celcius"
	
	def testNonNumeric(self):
		"""FahrenheittoCelcius should fail on non-numeric input"""
		badinputs = ["Text String", ("Text","Tuple"), ["Text", "List"],True,False,None]
		for Value in badinputs:
			self.assertRaises(conversions_refactored.NonNumericInputError, conversions_refactored.convert,self.fromUnit,self.toUnit, Value)
	def testLowerLimit(self):
		"""FahrenheittoCelcius should fail on input less than absolute zero"""
		self.assertRaises(conversions_refactored.LowerLimitError, conversions_refactored.convert, self.fromUnit, self.toUnit, -500)	

class FahrenheittoKelvinKnown(unittest.TestCase):
	fromUnit = "fahrenheit"
	toUnit = "kelvin"
	knownvalues = ((-459.67,0.00),(-364.00,53.15),(-202.00, 143.15), (-130.00, 183.15) ,(-22.00, 243.15), (86.00, 303.15), (212.00, 373.15), (392.00,473.15))
	
	def testFahrenheittoKelvinValues(self):
		"""FahrenheittoKelvin should succeed on all known inputs"""
		for input, output in self.knownvalues:
			result = conversions_refactored.convert(self.fromUnit,self.toUnit,input)
			self.assertEqual(result, output)
			
class FahrenheittoKelvinBadInput(unittest.TestCase):
	fromUnit = "fahrenheit"
	toUnit = "kelvin"
	def testNonNumeric(self):
		"""FahrenheittoKelvin should fail on non-numeric input"""
		badinputs = ["Text String", ("Text","Tuple"), ["Text", "List"],True,False,None]
		for Value in badinputs:
			self.assertRaises(conversions_refactored.NonNumericInputError, conversions_refactored.convert, self.fromUnit, self.toUnit, Value)
	def testLowerLimit(self):
		"""FahrenheittoKelvin should fail on input less than absolute zero"""
		self.assertRaises(conversions_refactored.LowerLimitError, conversions_refactored.convert,self.fromUnit, self.toUnit, -500)
		
class KelvintoCelciusKnown(unittest.TestCase):
	fromUnit = "kelvin"
	toUnit = "celcius"
	knownvalues = ((0.00, -273.15), (63.15,-210.00), (123.15, -150.00), (193.15, -80.00), (243.15, -30.00), (323.15, 50), (393.15, 120.00), (483.15, 210.00))
	def testKelvintoCelciusValues(self):
		"""KelvintoCelcius should succeed on all known inputs"""
		for input, output in self.knownvalues:
			result = conversions_refactored.convert(self.fromUnit,self.toUnit,input)
			self.assertEqual(result, output)
			
class KelvintoCelciusBadInput(unittest.TestCase):
	fromUnit = "kelvin"
	toUnit = "celcius"
	
	
	def testNonNumeric(self):
		"""KelvintoCelcius should fail on non-numeric input"""
		badinputs = ["Text String", ("Text","Tuple"), ["Text", "List"],True,False,None]
		for Value in badinputs:
			self.assertRaises(conversions_refactored.NonNumericInputError, conversions_refactored.convert, self.fromUnit,self.toUnit, Value)
	def testLowerLimit(self):
		"""KelvintoCelcius should fail on input less than absolute zero"""
		self.assertRaises(conversions_refactored.LowerLimitError, conversions_refactored.convert,self.fromUnit,self.toUnit, -1)	
		
class KelvintoFahrenheitKnown(unittest.TestCase):
	fromUnit = "kelvin"
	toUnit = "fahrenheit"
	knownvalues = ((0.00, -459.67), (63.15,-346.00), (123.15, -238.00), (193.15, -112.00), (243.15, -22.00), (323.15, 122.00), (393.15, 248.00), (483.15, 410.00))
	def testKelvintoFahrenheitValues(self):
		"""KelvintoFahrenheit should succeed on all known inputs"""
		for input, output in self.knownvalues:
			result = conversions_refactored.convert(self.fromUnit,self.toUnit,input)
			self.assertEqual(result, output)
			
class KelvintoFahrenheitBadInput(unittest.TestCase):
	fromUnit = "kelvin"
	toUnit = "fahrenheit"
	def testNonNumeric(self):
		"""KelvintoFahrenheit should fail on non-numeric input"""
		badinputs = ["Text String", ("Text","Tuple"), ["Text", "List"],True,False,None]
		for Value in badinputs:
			self.assertRaises(conversions_refactored.NonNumericInputError, conversions_refactored.convert, self.fromUnit,self.toUnit, Value)
	def testLowerLimit(self):
		"""KelvintoFahrenheit should fail on input less than absolute zero"""
		self.assertRaises(conversions_refactored.LowerLimitError, conversions_refactored.convert,self.fromUnit,self.toUnit, -1)	

class SanityTests(unittest.TestCase):
	def testUnitsSanity(self):
		units = (("celcius","fahrenheit"),
		("celcius","kelvin"),
		("fahrenheit","celcius"),
		("fahrenheit","kelvin"),
		("kelvin","celcius"),
		("kelvin","fahrenheit"),
		("miles","yards"),
		("miles","meters"),
		("yards","miles"),
		("yards","meters"),
		("meters","yards"),
		("meters","miles"))

		for i in units:
			fromUnit = i[0]
			toUnit = i[1]
			print fromUnit, toUnit
			for j in range(0,400):
				print "Units: ",j
				k = conversions_refactored.convert(fromUnit,toUnit,j)
				print "Units: ",k
				l = conversions_refactored.convert(toUnit,fromUnit,k)
				print "Units:",l
				l = int(l)
				print "Starting again"
		


if __name__ == '__main__':
    unittest.main()
	
