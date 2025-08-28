




file = input('Enter the file path please: ')
try:
    with open(file,'r') as f:
        content = f.read()
        print(content)
    with open(file,'a') as f:
        f.write('yo i need to tell you i love python am likeing it man!')
except FileNotFoundError:
    print("File not found")