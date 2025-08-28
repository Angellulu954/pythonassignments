def modify_file():
    # Ask user for filename
    filename = input("Enter the filename to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify content (example: make it uppercase)
        modified_content = content.upper()

        # Write modified content into a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"File processed successfully. Modified content saved in '{new_filename}'.")

    except FileNotFoundError:
        print("Error: The file was not found. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
modify_file()
