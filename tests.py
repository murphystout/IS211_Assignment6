import conversions
import unittest


class CelctoFarKnown(unittest.TestCase):
	knownvalues = ( (0,32),(7,44.6),(13,55.4),(16,60.8),(26,78.8),(29,84.2),(37,98.6),(52,125.6),(100,212),(138,280.4),(142,287.6),(145,293),(210,410))
	
	def testToFarKnownValues(self):
		"""CelctoFar should succeed for all known inputs"""
		for celc, far in self.knownvalues:
			result = conversions.convertCelciustoFahrenheit(celc)
			self.assertAlmostEqual(far, result)
	
class CelctoFarBadInput(unittest.TestCase):
	def testNonNumeric(self):
		"""CelctoFar should fail with non-numeric input"""
		badinputs = ["Text String", ("Text","Tuple"), ["Text", "List"],True,False,None]
		for member in badinputs:
			self.assertRaises(conversions.NonNumericInputError, conversions.convertCelciustoFahrenheit, member)

	def testLowerLimit(self):
		"""Celftofar should fail on input less than absolute zero"""
		self.assertRaises(conversions.LowerLimitError, conversions.convertCelciustoFahrenheit, -300)
		
class CelctoKelvinKnown(unittest.TestCase):
	knownvalues = ( (-273.15, 0), (-260,13.15), (-200,73.15), (-160, 113.15), (-100, 173.15), (0,273.15),(50,323.15),(100,373.15),(200,473.15),(250,523.15),(300,573.15))
	def testToKelvinKnownValues(self):
		"""CelctoKelvin should succeed on all known inputs"""
		for celc, kelv in self.knownvalues:
			result = conversions.convertCelsiustoKelvin(celc)
			self.assertAlmostEqual(kelv, result)

class CelctoKelvinBadInput(unittest.TestCase):
	def testNonNumeric(self):
		"""CelctoKelvin should fail on non-numeric input"""
		badinputs = ["Text String", ("Text","Tuple"), ["Text", "List"],True,False,None]
		for member in badinputs:
			self.assertRaises(conversions.NonNumericInputError, conversions.convertCelsiustoKelvin, member)
			
	def testLowerLimit(self):
		"""CelctoKelvin should fail on input less than absolute zero"""
		self.assertRaises(conversions.LowerLimitError, conversions.convertCelsiustoKelvin, -300)
	
class FahrenheittoCelciusKnown(unittest.TestCase):
	knownvalues = ((-459.67,-273.15),(-292.00,-180.00), (-94.00, -70.00), (-4.00, -20.00), (32.00, 0.00), (86.00, 30.00), (176.00, 80.00),(284.00,140.00), (572.00, 300))
	def testFahrenheittoCelciusValues(self):
		"""CelctoKelvin should succeed on all known inputs"""
		for input, output in self.knownvalues:
			result = conversions.convertFahrenheittoCelcius(input)
			self.assertAlmostEqual(result, output)
		
class FahrenheittoCelciusBadInput(unittest.TestCase):
	def testNonNumeric(self):
		"""FahrenheittoCelcius should fail on non-numeric input"""
		badinputs = ["Text String", ("Text","Tuple"), ["Text", "List"],True,False,None]
		for member in badinputs:
			self.assertRaises(conversions.NonNumericInputError, conversions.convertFahrenheittoCelcius, member)
	def testLowerLimit(self):
		"""FahrenheittoCelcius should fail on input less than absolute zero"""
		self.assertRaises(conversions.LowerLimitError, conversions.convertFahrenheittoCelcius, -500)	

class FahrenheittoKelvinKnown(unittest.TestCase):
	knownvalues = ((-459.67,0.00),(-364.00,53.15),(-202.00, 143.15), (-130.00, 183.15) ,(-22.00, 243.15), (86.00, 303.15), (212.00, 373.15), (392.00,473.15))
	def testFahrenheittoKelvinValues(self):
		
		"""FahrenheittoKelvin should succeed on all known inputs"""
		for input, output in self.knownvalues:
			result = conversions.convertFahrenheittoKelvin(input)
			self.assertAlmostEqual(result, output)
			
class FahrenheittoKelvinBadInput(unittest.TestCase):
	def testNonNumeric(self):
		"""FahrenheittoKelvin should fail on non-numeric input"""
		badinputs = ["Text String", ("Text","Tuple"), ["Text", "List"],True,False,None]
		for member in badinputs:
			self.assertRaises(conversions.NonNumericInputError, conversions.convertFahrenheittoKelvin, member)
	def testLowerLimit(self):
		"""FahrenheittoKelvin should fail on input less than absolute zero"""
		self.assertRaises(conversions.LowerLimitError, conversions.convertFahrenheittoKelvin, -500)
		
class KelvintoCelciusKnown(unittest.TestCase):
	knownvalues = ((0.00, -273.15), (63.15,-210.00), (123.15, -150.00), (193.15, -80.00), (243.15, -30.00), (323.15, 50), (393.15, 120.00), (483.15, 210.00))
	def testKelvintoCelciusValues(self):
		"""KelvintoCelcius should succeed on all known inputs"""
		for input, output in self.knownvalues:
			result = conversions.convertKelvintoCelcius(input)
			self.assertAlmostEqual(result, output)
			
class KelvintoCelciusBadInput(unittest.TestCase):
	def testNonNumeric(self):
		"""KelvintoCelcius should fail on non-numeric input"""
		badinputs = ["Text String", ("Text","Tuple"), ["Text", "List"],True,False,None]
		for member in badinputs:
			self.assertRaises(conversions.NonNumericInputError, conversions.convertKelvintoCelcius, member)
	def testLowerLimit(self):
		"""KelvintoCelcius should fail on input less than absolute zero"""
		self.assertRaises(conversions.LowerLimitError, conversions.convertKelvintoCelcius, -1)	
		
class KelvintoFahrenheitKnown(unittest.TestCase):
	knownvalues = ((0.00, -459.67), (63.15,-346.00), (123.15, -238.00), (193.15, -112.00), (243.15, -22.00), (323.15, 122.00), (393.15, 248.00), (483.15, 410.00))
	def testKelvintoFahrenheitValues(self):
		"""KelvintoFahrenheit should succeed on all known inputs"""
		for input, output in self.knownvalues:
			result = conversions.convertKelvintoFahrenheit(input)
			self.assertAlmostEqual(result, output)
			
class KelvintoFahrenheitBadInput(unittest.TestCase):
	def testNonNumeric(self):
		"""KelvintoFahrenheit should fail on non-numeric input"""
		badinputs = ["Text String", ("Text","Tuple"), ["Text", "List"],True,False,None]
		for member in badinputs:
			self.assertRaises(conversions.NonNumericInputError, conversions.convertKelvintoFahrenheit, member)
	def testLowerLimit(self):
		"""KelvintoFahrenheit should fail on input less than absolute zero"""
		self.assertRaises(conversions.LowerLimitError, conversions.convertKelvintoFahrenheit, -1)	

class SanityTests(unittest.TestCase):
	def testKelvinSanity(self):
		for i in range(0,400):
			i = float(i)
			celcius = conversions.convertKelvintoCelcius(i)
			far = conversions.convertCelciustoFahrenheit(celcius)
			kelvin = conversions.convertFahrenheittoKelvin(far)
			self.assertAlmostEqual(i, kelvin)
	
	def testCelsiusSanity(self):
		for i in range(-273,100):
			i = float(i)
			kelvin = conversions.convertCelsiustoKelvin(i)
			far = conversions.convertKelvintoFahrenheit(kelvin)
			celcius = conversions.convertFahrenheittoCelcius(far)
			self.assertAlmostEqual(i, celcius)
	
	def testFarSanity(self):
		for i in range(-450,212, 5):
			i = i * 1.00
			celcius = conversions.convertFahrenheittoCelcius(i)
			far = conversions.convertCelciustoFahrenheit(celcius)
			far = round(far)
			self.assertAlmostEqual(i,far)

if __name__ == '__main__':
    unittest.main()
	
