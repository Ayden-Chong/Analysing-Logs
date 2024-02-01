import os

listoflogs = os.listdir("./Logs")
errorcount = 0
infocount = 0
warningcount = 0

for logs in listoflogs:
    with open(f"./Logs/{logs}") as file:
        for line in file:
            if line.find("ERROR") != -1:
                errorcount += 1
            elif line.find("INFO") != -1:
                infocount += 1 
            elif line.find("WARNING") != -1:
                warningcount += 1

with open("Report.txt", "w") as file:
    file.write(f"Error Count: {errorcount}\n")
    file.write(f"Info Count: {infocount}\n")
    file.write(f"Warning Count: {warningcount}\n")







































# Get a list of all log files in the Logs directory
# Hint: Use the os.listdir() function

# Process each log file
# Hint: Use a for loop to iterate over the log files

    # Initialize counters for each type of event
    # Hint: You can use simple variables for this

    # Open the log file
    # Hint: Use the 'with open()' statement to open the file for reading

        # Read each line in the log file
        # Hint: Use a for loop to iterate over the lines in the file

            # Count the number of each type of event
            # Hint: Use if statements and the 'in' keyword to check if a string is in the line

    # Write the counts to the report file
    # Hint: Use the 'with open()' statement to open the file for writing
    # Hint: Use the 'write()' method to write a line to the file
