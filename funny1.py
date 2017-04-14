from sys import argv

script , user_name1 = argv
promt = '>'

print "What's your name?"
Name = raw_input(promt)
print "Hi %s, I'm %s" % (Name , user_name1)
print "I'd like to ask you a few question."
print "How old are you, %s?" % (Name)
Age = raw_input(promt)
print "Where do you live %s?" %(Name)
Lives = raw_input (promt)
print "What is your job?"
Job = raw_input (promt)
print "Do you like me %s?" % (Name)
likes = raw_input(promt)

print """
Alright, so you are %r.
You are %r years old and you live in %r.
You have a job - %r. And special, you said %r about liking me.
Thanks your answer!
""" % (Name , Age , Lives , Job , likes)