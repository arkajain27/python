'''
import sys

print(f"{len(sys.argv)}")
print(f"{type(sys.argv)}")
print(f"argument 1 = {sys.argv[0]}")

if len(sys.argv) < 2:
    print("To few arguments")
elif len(sys.argv) > 2:
    sys.exit("To many arguments")   

print("Hello my name is", sys.argv[1])
'''
for i in range(5):
    print(i)