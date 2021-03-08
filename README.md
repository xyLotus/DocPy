<h1 align="center">DocumentPy</h1>

<p align="center">
  <image src="https://img.shields.io/badge/Implementation-Python%203.9-%2300A3E0?style=flat-square">
  <image src="https://img.shields.io/badge/version-0.5-blue">
  <image src="https://img.shields.io/badge/Work%20In%20Progress-True-success">
  <image src="https://img.shields.io/tokei/lines/github/xyLotus/DocumentPy?label=Total%20lines&style=flat-square">
</p>

<p>DocumentPy is a Python application that runs in a commandline interface environment, made for creating HTML documents.</p>

## Usage
![Preview](https://user-images.githubusercontent.com/59749700/110297228-8af49f80-7ff3-11eb-9e83-e92aa595b7e8.gif)
DocumentPy, as already said, is a commandline interface environment where you can design your own HTML document or HTML documentations.
If you, for example, have some kind of new project on the line and want to quickly write a documentation for it, then don't worry, DocumentPy is your best friend!

## Command Tables
### Document Editing Commands
| Command       | Arguments         | Purpose                                                  |
| ------------- | ----------------- | -------------------------------------------------------- |
| `paragraph, p`  | *Text*              | Creating a paragraph with a given text                   |
| `header, h`     | *Size, Text*       | Creating a header with the given text and size           |
| `coloring, c `  | *Color*            | Changing the auto coloring of a HTML Document Element    |
| `background, bg`| *Background_Color*| Changes the doc's background to the given bg color     | 


### Document Information Editing Commands
| Command       | Arguments         | Purpose                                                  |
| ------------- | ----------------- | -------------------------------------------------------- |
| `lang`          | *New_Language*      | Changes document language to given lang                  |
| `title`         | *New_Title*         | Changes the title to the given title in the document     |
| `charset`       | *New_Charset*       | Changes the charset to the given charset in the document |
| `author`        | *New_Author*        | Changes the author to the given author in the document   |


### Commandline IO & Flow Control Commands
| Command       | Arguments         | Purpose                                                  |
| ------------- | ----------------- | -------------------------------------------------------- |
| `out`           | *Output_Text*     | Outputs text into the commandline interface environment|
| `cls`           |                   | Clears all the commandline interface input/output      |
| `exit`          |                   | Exits the program                                      |
| `getfile`       |                   | Outputs the current file the commandline is workng in  |

## Requirements
- **[Python 3.9](https://www.python.org)**
- **[Python, bs4](https://pypi.org/project/beautifulsoup4)**
- **[Python, stdlib](https://docs.python.org/3/library)**

## Contact
Discord: Lotus#1095
