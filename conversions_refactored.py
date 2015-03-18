# Argparse didn't seem to work with the unittests, so commenting out
# import argparse
# parser = argparse.ArgumentParser(description = 'Unit Conversions for Distance: Meters, Yards, Miles and Temperature: Kelvin, Celcius, Fahrenheit')
# parser.add_argument("--fromunit", type = str, help = "Unit to Convert FROM")
# parser.add_argument("--tounit",type = str, help = "Unit to Convert TO")
# parser.add_argument("--value", type = float, help = "Value to convert")
# args = parser.parse_args()
# fromUnit = args.fromunit
# toUnit = args.tounit
# value = args.value

class conversionError(Exception): pass
class NonNumericInputError(Exception): pass
class LowerLimitError(Exception): pass
class IncorrectUnitException(Exception): pass



# Create dictionary of unit conversions in the form of {(fromUnit,toUnit),(formula)}
unit_dictionary = {
("celcius","fahrenheit"):("x * 9.000/5.000 + 32.00"),
("celcius","kelvin"):("x + 273.15"),
("fahrenheit","celcius"):("(x - 32.00)* 5.00/9.00"),
("fahrenheit","kelvin"):("(x + 459.67) * 5.00/9.00"),
("kelvin","celcius"):("x - 273.15"),
("kelvin","fahrenheit"):("x * 9.00/5.00 - 459.67"),
("miles","yards"):("x * 1760.00"),
("miles","meters"):("x * 1609.34"),
("yards","miles"):("x / 1760.00"),
("yards","meters"):("x * 0.9144"),
("meters","yards"):("x * 1.09361"),
("meters","miles"):("x / 1609.34")
}
		
def convert(fromUnit,toUnit,value):
	if(type(value) is not int and type(value) is not long and type(value) is not float):
		raise NonNumericInputError, 'Value input is non-numeric!'
	elif(unit_dictionary[(fromUnit,toUnit)] is None):
		raise IncorrectUnitException, 'Incorrect Unit Matching, Try Again'
	elif (fromUnit == "kelvin" and value < 0) or (fromUnit == "celcius" and value < -273.15) or (fromUnit == "fahrenheit" and value < -459.67):
		raise LowerLimitError, 'Temperature value is lower than absolute zero!'
	elif ((fromUnit == "miles" or fromUnit == "yards" or fromUnit == "meters") and value < 0):
		raise LowerLimitError, 'Distance unit is negative!'
	else:
		x = value
		result = eval(unit_dictionary[(fromUnit,toUnit)])
		return round(result,2)
		
# result_value = convert(fromUnit,toUnit,value)

# print value ,"in", fromUnit, "converts to" ,result_value, "in ", toUnit
