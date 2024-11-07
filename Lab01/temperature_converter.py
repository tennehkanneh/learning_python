BASE = 32
CONVERSION_FACTOR = 9 / 5

celsisuTemp = 24
fahrenheitTemp = 98.6

#fahrenheitTemp = celsiusTemp * CONVERSION_FACTOR + BASE;
celsiusTemp = (fahrenheitTemp - BASE) / CONVERSION_FACTOR;

print("Celsius Temperature: " + str(celsiusTemp));
print("Fahrenheit Equivalent: " + str(fahrenheitTemp));
