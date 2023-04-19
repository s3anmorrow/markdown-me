# module imports
import os
import subprocess
import sys
import re

# -------------------------------------------- private methods
def getFolders(folderPath):
    foldersList = []
    # get list of all files / folders in path
    entities = os.listdir(folderPath)
    # get list of only the folders
    for entity in entities:
        if os.path.isdir(folderPath + entity) and entity.startswith("unit"):
            foldersList.append(entity)

    return foldersList

# -------------------------------------------- main method
def main():
    print("\033[0;31m","------------------------------------------------------------")
    print("\033[0;31m","MD-ME -> Markdown Me v1.0 - Sean Morrow [Apr 2023]")

    unitFolders = getFolders("./")
    unitFolders.append(".")

    for unitFolder in unitFolders:

        # get the full path
        path = os.path.dirname(os.path.realpath(__file__)) + "/" + unitFolder + "/"

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

                print("\033[0;32m","MD-ME -> formatting md : " + mdDoc)

                # break content into lines
                lines = content.splitlines()
                content = ""
                bulleting = True
                coding = False

                # go through each line
                for line in lines:
                    line = line.replace("**Lesson Plan \>**", "# Lesson Plan \>")
                    line = line.replace("**Instructional Procedures:**", "## Instructional Procedures:")
                    line = line.replace("> \> ", "\t- ")
                    line = line.replace("\> ", "- ")
                    line = line.replace("> ", "")
                    line = line.replace("\`\`\`","```")
                    line = line.replace("`\\","`")

                    if (bulleting) and ("**" not in line) and ("#" not in line) and (line != ""):
                        line = "- " + line

                    # remove all escape characters from code blocks
                    if (coding):
                        line = line.replace("\[", "[")
                        line = line.replace("\]", "]")
                        line = line.replace("\`", "`")
                        line = line.replace('\\"', '\"')
                        line = line.replace("\<", "<")
                        line = line.replace("\>", ">")
                        line = line.replace("\-", "-")
                        line = line.replace("\_", "_")
                        line = line.replace("\*", "*")
                        line = line.replace("\#", "#")
                        line = line.replace("\$", "$")
                        line = line.replace("\\\\", "\\")
                    else:
                        line = line.replace("\<div-","\<div\>")
                        line = line.replace("\<body-","\<body\>")
                        line = line.replace("\<span-","\<span\>")
                        line = line.replace("\<i-","\<i\>")

                    newline = "\n"
                    if (line == ">"):
                        line = ""

                    if (coding) and (line == ""):
                        line = ""
                        newline = ""
                    
                    content = content + line + newline

                    # is it time to stop adding bullets to all lines? (only done in header of lesson plan)
                    if ("## Instructional Procedures:" in line):
                        bulleting = False
                    if ("**Materials and Equipment" in line):
                        bulleting = True

                    if ("```" in line):
                        coding = not coding

                # write the cleaned up content back to the markdown document
                with open(path + mdDoc, "w") as file:
                    file.write(content)

    print("\033[0;31m","MD-ME -> markdown me complete")

main()