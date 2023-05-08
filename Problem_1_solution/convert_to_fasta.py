# Open the input file for reading
with open("1601456737847_Plants_Release42_triticum_dicoccoides.txt", "r") as input_file:
    # Open the output file for writing
    with open("output.fa", "w") as output_file:
        # Read the contents of the input file
        content = input_file.readlines()
        # Loop over the lines in the input file
        for i, line in enumerate(content):
            # If the line starts with ">", it is a sequence identifier
            if line.startswith(">"):
                # Write the sequence identifier to the output file
                output_file.write(line)
            # Otherwise, it is a genomic sequence
            else:
                # Write the genomic sequence to the output file in FASTA format
                output_file.write(">sequence_" + str(i) + "\n")
                output_file.write(line + "\n")

