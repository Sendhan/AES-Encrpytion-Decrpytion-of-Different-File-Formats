def file_read(filename):
    with open(filename, 'rb') as file:
        filedata = file.read()
        return filedata

def file_write(filename, filedata):
    with open(filename, 'wb') as file:
        file.write(filedata)
