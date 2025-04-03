# writting a file
filepath = "sample.thcxt"
content_to_write = "Python is a programming language. It is mostly used in back-end development."

try:
    with open(filepath, "w") as file:
        file.write(content_to_write)
        print(f"Content has been written to '{filepath}' successfully.")
except Exception as e:
     print(f"An error occurred: {e}")

    #  reading the file
try:      
  with open(filepath, 'r') as file:
    content_to_read =file.read()
    print("content of the file:")
    print(content_to_read)
except Exception as e:
 print(f"Can't be read: {e}")

    