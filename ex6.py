x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
#print "There are 10 types of people."
print x
#print "Those who know binary and those who do_not."
print y
#print "I said: There are 10 types of people"
print "I said: %r." % x
#print "I also said: 'Those who know binary and those who do_not.'."
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#print "Isn't that joke so funny?! False"
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
#print "This is the left side of ... a string with a right side"
print w + e