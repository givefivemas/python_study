from shlex import split

string = input("Enter a string: ")

print("Symbols: " + str(len(string)))

print("Words: " + str(len(split(string))))

print("A letters: " + str(string.count("а")))