
MILES_IN_KILOMETERS = 1.60935
amount_of_miles = 2.5

conversion_miles_to_kilometers = amount_of_miles * MILES_IN_KILOMETERS

# When concatinating floats str() or some other conversion must be used
print("Distance in miles: " + str(amount_of_miles));
print("Distance in Kilometers: " + str(conversion_miles_to_kilometers));