# Markdown Me
Converts my lesson plans from DOCS to Markdown for the big migration away from stupid MS Word (why did it take me so long?)

## Usage
Copy the extract.py file into each unit folder of a course and run with command:
```
python md-me.py
``` 
The script will go through all word document files and convert them to markdown and do some minor formatting fixes.

Some tweaks that will need to be done with the generated md files:
- all markdown characters (-,>,<,*,#,etc) will be escaped with a backslash - this is required for normal text but in code blocks (marked with ```) will be make the code unreadable
- indentation will need to be done to get the tabbing correct
- code blocks will be formatted correctly if a ''' is added around the code blocks in the word document prior to conversion. Can be automated in word: 
    - do an "Advanced Find and Replace" searching for New Courier font (font used for all code snippets in my lesson plans)
    - do replace all with ```^l^&```^l

Good markdown references: 
- https://pandao.github.io/editor.md/en.html
- https://guides.github.com/features/mastering-markdown/
- https://www.markdownguide.org/cheat-sheet/ 

## Requirements
- Pandoc (https://pandoc.org/installing.html)
- Python 3 (https://www.python.org/downloads/ or install via MS Store)