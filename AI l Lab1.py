import os

file_name = "Chaity.txt"
content_to_write = "Hello, I am your friend."

if os.path.exists(file_name):
    f = open("Chaity.txt", "a")
    f.write(content_to_write)
    f.close()

    f = open("Chaity.txt", "r")
    print(f.read())
    f.close()


    os.remove(file_name)
    print(f"{file_name} deleted successfully.")
else:
    print(f"There is no file named '{file_name}'.")
