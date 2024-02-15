command = input('enter an operation: ').lower()
while(command not in ("c", "r", "u", "d", "q")):
    command = input('please enter a valid operation: ').lower()
if command == "c":
    print("bark")
elif command == "r":
    print("herro")
elif command == "u":
    print("woof")
elif command == "d":
    print("pew pew")
elif command == "q":
    print("grrrrr")
print("end of program")