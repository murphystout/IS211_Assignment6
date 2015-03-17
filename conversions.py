class calculationsError(Exception): pass
class NonNumericInputError(Exception): pass
class LowerLimitError(Exception): pass

def convertCelciustoFahrenheit(input):
	if (not type(input) == int) and (not type(input) == float) and (not type(input) == long):
		raise NonNumericInputError, 'Non Numeric Input:'
	if input < -273.15:
		raise LowerLimitError, 'Lower Limit Error. Input less than 273.15'
	return round(input * 9.0/5.0 + 32.0,2)

def convertCelsiustoKelvin(input):
	if (not type(input) == int) and (not type(input) == float) and (not type(input) == long):
		raise NonNumericInputError, 'Non Numeric Input:'
	elif input < -273.15:
		raise LowerLimitError, 'Lower Limit Error. Input less than 273.15'
	else:
		return round(input + 273.15,2)
	
