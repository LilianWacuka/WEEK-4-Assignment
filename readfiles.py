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


    # user input for file
def read_file():
        filename = input("input the file to read:")
        try:
            with open(filename, "r")as file:
                content = file.read()
                print("\ncontent of the file:\n")
                print(content)
        except Exception as e:
            print(f"an error occured: {e}")
        except FileNotFoundError:
            print(f"❌ Error: The file '{filename}' was not found.")
        except Exception as e:
            print(f"⚠️ An error occurred: {e}")

            # calling the function
read_file()

        

