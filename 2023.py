import sys

if len(sys.argv) < 2:
    print("To few arguments")
elif len(sys.argv) > 2:
    sys.exit("To many arguments")
    
print("Hello my name is", sys.argv[1])