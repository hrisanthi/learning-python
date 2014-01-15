cars = 100
space_in_car = 4
drivers = 30
passengers = 90

cars_driven = drivers
cars_not_driven = cars - drivers

carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven


print "There are",cars,"cars available."
print "There are only",drivers,"drivers available."
print "We can transpaort",carpool_capacity,"people today."
print "We have %d to carpool today." %passengers
print "We need to put %d passengers in each of the %d cars." %(average_passengers_per_car, cars_driven)