class calculationsError(Exception): pass
class NonNumericInputError(Exception): pass
class LowerLimitError(Exception): pass

def convertCelciustoFahrenheit(input):
	if (not type(input) == int) and (not type(input) == float) and (not type(input) == long):
		raise NonNumericInputError, 'Non Numeric Input:'
	if input < -273.15:
		raise LowerLimitError, 'Lower Limit Error. Celcius Input less than -273.15'
	else:
		return round(input * 9.0/5.0 + 32.0,2)

def convertCelsiustoKelvin(input):
	if (not type(input) == int) and (not type(input) == float) and (not type(input) == long):
		raise NonNumericInputError, 'Non Numeric Input:'
	elif input < -273.15:
		raise LowerLimitError, 'Lower Limit Error. Celcius Input less than -273.15'
	else:
		return round(input + 273.15,2)
	
def convertFahrenheittoCelcius(input):
	if (not type(input) == int) and (not type(input) == float) and (not type(input) == long):
		raise NonNumericInputError, 'Non Numeric Input:'
	if input < -459.67:
		raise LowerLimitError, 'Lower Limit Error. Fahrenheit Input less than -459.67'
	else:
		return round((input - 32.0) * 5.0/9.0,2)

def convertFahrenheittoKelvin(input):
	if (not type(input) == int) and (not type(input) == float) and (not type(input) == long):
		raise NonNumericInputError, 'Non Numeric Input:'
	if input < -459.67:
		raise LowerLimitError, 'Lower Limit Error. Fahrenheit Input less than -459.67'
	else:
		return round((input + 459.67) * 5/9,2)
	
		
def convertKelvintoCelcius(input):
	if (not type(input) == int) and (not type(input) == float) and (not type(input) == long):
		raise NonNumericInputError, 'Non Numeric Input:'
	if input < 0:
		raise LowerLimitError, 'Lower Limit Error. Kelvin Input less than 0'
	else:
		return round(input - 273.15,2)
	
def convertKelvintoFahrenheit(input):
	if (not type(input) == int) and (not type(input) == float) and (not type(input) == long):
		raise NonNumericInputError, 'Non Numeric Input:'
	if input < 0:
		raise LowerLimitError, 'Lower Limit Error. Kelvin Input less than 0'
	else:
		return round(input * 9.0/5.0 - 459.67,2)
		
