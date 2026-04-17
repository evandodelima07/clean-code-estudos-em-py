#Cópia entre listas

def copy_chars(source, destination):
    for item in source:
        destination.append(item)

source = ['a', 'b', 'c']
destination = []

copy_chars(source, destination)
print(destination)