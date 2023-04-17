# module imports
import os
import subprocess
import sys
import re

# -------------------------------------------- main method
def main():
    print("\033[0;31m","------------------------------------------------------------")
    print("\033[0;31m","MD-ME -> Markdown Me v1.0 - Sean Morrow [Apr 2023]")

    # get the full path
    path = os.path.dirname(os.path.realpath(__file__)) + "/"

    # get list of word document files in path
    wordDocs = []
    mdDocs = []
    for file in os.listdir(path):
        if file.endswith(".docx") and not file.startswith("~$"):
            wordDocs.append(file)
            mdDocs.append(file[:-5] + ".md")

    # go through each word document and convert it to markdown
    for wordDoc in wordDocs:
        print("\033[0;32m","MD-ME -> converting to md : " + wordDoc)
        p = subprocess.Popen(["pandoc", "-f", "docx", "-t", "markdown", path + wordDoc, "-o", path + wordDoc[:-5] + ".md"])   
        p.wait()

    # go through each markdown document and clean up content / formatting
    for mdDoc in mdDocs:
        # open each markdown document
        with open(path + mdDoc, "r") as file:  
            content = file.read()

            print("\033[0;32m","MD-ME -> formatting md : " + wordDoc)

            # break content into lines
            lines = content.splitlines()
            content = ""
            # go through each line
            for line in lines:
                line = line.replace("**Lesson Plan \>**", "# Lesson Plan \>")
                line = line.replace("**Instructional Procedures:**", "## Instructional Procedures:")
                line = line.replace("> \> ", "\t- ")
                line = line.replace("\> ", "- ")
                line = line.replace("> ", "- ")
                
                if (line != ">"):
                    content = content + line + "\n"

            # write the cleaned up content back to the markdown document
            with open(path + mdDoc, "w") as file:
                file.write(content)

    print("\033[0;31m","MD-ME -> markdown me complete")

main()