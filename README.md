# Questions-of-python-for-bioinformatics


{
  "cells": [
    {
      "cell_type": "markdown",
      "id": "3e90fd49",
      "metadata": {
        "id": "3e90fd49"
      },
      "source": [
        "# Technical Assignment : Bioinformatics Engineer Intern\n",
        "\n",
        "### Allotted time : 2 days"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "fcd1ea22",
      "metadata": {
        "id": "fcd1ea22"
      },
      "source": [
        "### Instructions:  \n",
        "\n",
        "1. Please read the problem statement(s) carefully.\n",
        "2. Please explain your code/solution with comments.\n",
        "3. You are free to use internet resources to arrive at a solution."
      ]
    },
    {
      "cell_type": "markdown",
      "id": "b47fa8f6",
      "metadata": {
        "id": "b47fa8f6"
      },
      "source": [
        "## Problem Statement 1:  \n",
        "\n",
        "A bench scientist is required to identify consensus sequence in a genetic data using an open-source software called MEME suite. It takes input in the form of a sequence file and returns a consensus sequence based on the conserved patterns in the genome.  \n",
        "\n",
        "The challenge is the input data is in a .txt file and the API they saw only takes input in .fasta/.fa format.  \n",
        "\n",
        "Your task is to convert *1601456737847_Plants_Release42_triticum_dicoccoides.txt* into a .fasta/.fa file that will be used to generate the consensus sequence on MEME suite. \n",
        "\n",
        "NOTE: The input file has been provided along with the question bank.\n",
        "\n",
        "\n",
        "### Expected output:  \n",
        "\n",
        "A .fasta/.fa file containing the genomic sequence and description for all sequences\n",
        "\n",
        "\n",
        "### FASTA format description\n",
        "\n",
        "A sequence in FASTA format consists of:  \n",
        "\n",
        "1. One line starting with a \">\" sign, followed by a sequence identification code.\n",
        "        - It is optionally be followed by a textual description of the sequence. Since it is not part of the official description of the format, software can choose to ignore this, when it is present.\n",
        "2. One or more lines containing the genomic sequence itself.\n",
        "3. A file in FASTA format may comprise more than one sequence"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "237e72fd",
      "metadata": {
        "id": "237e72fd"
      },
      "source": [
        "## Problem Statement 2:  \n",
        "\n",
        "#### Required knowledge -\n",
        "- SQL - Joins, Nested Queries\n",
        "- Python - functions, recursions, loops, nested loops\n",
        "\n",
        "\n",
        "You are given an input file \"tasks_info.csv\" which contains some data which needs to be processed in certain ways.\n",
        "\n",
        "You're required to: \n",
        "\n",
        "- Load & parse the csv file into a pandas dataframe\n",
        "- Install 'pandasql' in your local system, which can enable you to write & execute SQL queries over a parsed dataframe\n",
        "- Write an SQL statement to extract all the 'task_ids' from csv, which belongs to those \"task_groups\" for which total no of 'success' tasks is more than 2.\n",
        "    - For example, 'task_group_id'='1' contains 3 successful tasks. Hence, all task_ids belonging to 'task_group_id'='1' \n",
        "      should be included in the output, along with other output task_ids, if any.\n",
        "- Finally, Execute this SQL over the dataframe, and output the list of such required task ids.\n",
        "\n",
        "NOTE: The input file has been provided along with the question bank.\n",
        "\n",
        "\n",
        "### Expected output:  \n",
        "\n",
        "A list of task ids."
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Problem Statement 3:\n",
        "\n",
        "WORD PLAY :-\n",
        "\n",
        "You are required to write a function in python which does the following operations sequentially, on a given string input.\n",
        "\n",
        "Suppose, given input = \"word1 word2 word3\"\n",
        "\n",
        "a) For each word present in the input: Pick the odd position characters and move them ahead of the even-position characters.\n",
        "- Example: for word \"word1\", the resultant word should be \"wr1od\" (w->r->1  at odd positions followed by o->d)\n",
        "\n",
        "b) Reverse each word formed above.\n",
        "- Example: (\"wr1od\" -> \"do1rw\")\n",
        "\n",
        "c) Take the first three characters of each of the reversed words & combine all of them using dashes('-') to form one final single string.\n",
        "- Example: \"do1\" + \"do2\" + \"do3\" = \"do1-do2-do3\"\n",
        "\n",
        "d) Return the final string as function output.\n",
        "    \n",
        "### Expected output:  \n",
        "\n",
        "A processed string"
      ],
      "metadata": {
        "id": "3_Zax1uDmsYZ"
      },
      "id": "3_Zax1uDmsYZ"
    },
    {
      "cell_type": "code",
      "source": [
        "#Enter code here"
      ],
      "metadata": {
        "id": "cOXmcS02mqMG"
      },
      "id": "cOXmcS02mqMG",
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.10.2"
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}
