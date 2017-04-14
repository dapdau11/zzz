from sys import argv
script, filename = argv
#open the file need to read
txt = open(filename)

print "Here's your file %r:" % filename
#read: read content of file, print it
print txt.read()
txt.close()
print "Type the file name again:"
#solution 2: raw_input
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
