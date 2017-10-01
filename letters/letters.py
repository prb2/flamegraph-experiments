import sys

if len(sys.argv) != 2:
    print "Usage: \n"
    print "\t$ python letters.py <filename> > output.txt\n"
    print "Where <filename> is the path to a text file containing one word per line."
    print "Then, output.txt can be used as input to the flamegraph script."
else:
    f = open(sys.argv[1])

    for word in f.readlines():
        line = ""
        for letter in word[:-1]: # :-1 to get rid of the trailing newline char
            line += letter + ";"

        print(line[0:-1] + " 1")

    f.close()

