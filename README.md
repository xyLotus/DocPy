<h1 align="center">DocumentPy</h1>

<p align="center">
  <image src="https://img.shields.io/badge/Implementation-Python%203.9-%2300A3E0?style=flat-square">
</p>


<p>DocumentPy is a Python application that runs in a commandline interface environment, made for creating HTML documents.</p>

## Document Editing Commands
| Command       | Arguments         | Porpuse                                                  |
| ------------- | ----------------- | -------------------------------------------------------- |
| ´paragraph, p´  | Text              | Creating a paragraph with a given text                   |
| header, h     | Size, Text        | Creating a header with the given text and size           |
| coloring, c   | Color             | Changing the auto coloring of a HTML Document Element    |

## Document Information Editing Commands
| Command       | Arguments         | Porpuse                                                  |
| ------------- | ----------------- | -------------------------------------------------------- |
| lang          | New_Language      | Changes document language to given lang                  |
| title         | New_Title         | Changes the title to the given title in the document     |
| charset       | New_Charset       | Changes the charset to the given charset in the document |
| author        | New_Author        | Changes the author to the given author in the document   |

## Commandline IO & Flow Control Commands
| Command       | Arguments         | Porpuse                                                  |
| ------------- | ----------------- | -------------------------------------------------------- |
| out           | Output_Text       | Outputs text into the commandline interface environment  |
| cls           |                   | Clears all the commandline interface input/output        |
| exit          |                   | Exits the program                                        |
| getfile       |                   | Outputs the current file the commandline is workng in    |
