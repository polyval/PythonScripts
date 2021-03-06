import sys
inname, outname = sys.argv[1:3]

def warnings_filter(insequence):
    for l in insequence:
        if 'WARNING' in l:
            yield l.replace('\tWARNING', '')

with open(inname) as infile:
    with open(outname, "w") as outfile:
        filter = warnings_filter(infile) 
        # generator object, has __iter__ and __next__(next in Python 2.x) methods
        for l in filter:
            outfile.write(l)
