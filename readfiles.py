# modifying  a file sample.txt
inputfilepath= "sample.txt"
outputfilepath= "modified-sample.txt"
# writing a file
contenttowrite= "Learning Python is fun!. It is a versatile language."
try:
    with open(outputfilepath, "w") as outputfile:
        outputfile.write(contenttowrite)
        print(f"Content has been written to '{inputfilepath}'sucessfully.")
except Exception as e:
    print(f"An error occurred: {e}")

    # Appending a file
additional_content = " Python is widely used in web development, data science, and more."
try:
    with open(outputfilepath, "a") as inputfile:
        inputfile.write(additional_content)
        print(f"Content has been appended to '{outputfilepath}' successfully.")
        print("Content of the file:")
        print(additional_content)
except Exception as e:
    print(f"An error occurred: {e}")

    # reading the file
    try:
        with open(inputfilepath, "r") as file:
         additional_content = file.read()
        print("Content of the file:")
        print(additional_content)
    except Exception as e:
            print(f"Can't be read: {e}")
## Reading the output file
try:
    with open(outputfilepath, "r") as outputfile:
        modified_content = outputfile.read()
        print("Content of the output file:")
        print(modified_content)
except Exception as e:
    print(f"An error occurred while reading the output file: {e}")

