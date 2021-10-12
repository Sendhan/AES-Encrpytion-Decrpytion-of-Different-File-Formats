import uuid

def generate_txt_file(filename, number_of_lines) :
    with open(filename, 'w') as file:
        for i in range(number_of_lines):
            randomline = str(uuid.uuid4())
            file.write(randomline + "\n")
