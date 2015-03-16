class calculationsError(Exception): pass
class NonNumericInputError(Exception): pass
class LowerLimitError(Exception): pass

def convertCelciustoFahrenheit(input):
	return float(input * (9/5) + 32)

def convertCelsiustoKelvin(input):
	return float(input + 273.15)

	
