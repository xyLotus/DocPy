"""
This is the DocPy module made for creating HtmlDocuments in
a commandline interface environment.
It is also very handy for creating HTML Documentations.
"""

"""
NOTE TO MYSELF (READ)

Catch index error @method = p, paragraph
"""

__author__ = 'Lotus'
__version__ = 0.1

# Imports
import os

# Create Back-up File
if not os.path.isfile(f'{os.getcwd()}\\backup.txt'):
    with open('backup.txt', 'x'):
        pass

# Global Functions
def call_method(cls: object, function: str, args: list):
    """ Calls method from given class, with given arguments """
    try:
        getattr(cls, function)(args)
    except Exception:
        getattr(cls, function)()

def error(txt: str):
    """ Outputs string in error format. """
    print(f'[ERROR] - ({txt})')


# Classes
class Document:
    """ Document class responsible for assigning mandatory doc vars. """
    title = ''
    lang = ''
    author = ''
    charset = ''
    content = ''
    css_file = ''
    body_content = ''


doc = Document()

def append_content(additional_content: str):
    """ Appends the content (@file = htmldoc, @tag =<body>). """
    doc.content += additional_content + '\n'


class FileStream:
    """ FileStream Class responsible for file handling. """
    def __init__(self):
        #====FileDataVars====#
        self.open_bool = False
        self.file = ''
        self.file_str = ''
        #====================#

        #===FileContentVar===#
        cwd = os.getcwd()
        try:
            with open(f'{cwd}\\skeleton.html', 'r') as f:
                self.skeleton = f.read()
        except Exception as e:
            # Error Stacktraceback & Exit
            error(e)
            exit()
        #====================#

    def write(self, text):
        """ Write to file. """
        with open(self.file, 'a') as f:
            f.write(text)

    def init_skeleton(self):
        """ Method that writes skeleton to given file. """
        with open(self.file, 'w') as f:
            f.write(self.skeleton)
        
    def get_content(self, file_name: str):
        with open(file_name, 'r') as f:
            return f.read()
        
    def backup(self):
        with open('backup.txt', 'w') as f:
            f.write(self.get_content(self.file))


file_stream = FileStream()

class Commands:
    """ Commands class responsible for storing methods, that will get reflected. [See: C# Reflection] """
    def __init__(self):
        self.auto_coloring = True
        self.auto_color = 'black'
    
    #====FileCommands====#
    def open(self, args):
        """ Method that opens the given file. """
        file_stream.open_bool = True
        cwd = os.getcwd()
        if os.path.isfile(f'{cwd}\\{args[0]}'):
            print(f'Opening [{args[0]}]...')
            file_stream.file = args[0]

            with open(file_stream.file, 'r') as f:
                file_stream.file_str = f.read()
        else:
            error(f'Couldnt find [{args[0]}]')
        
        print(f'Opened [{args[0]}]!')

    def new(self, args):
        """ Method that creates a new file. """
        cwd = os.getcwd()
        if not os.path.isfile(f'{cwd}\\{args[0]}'):
            print(f'Creating [{args[0]}]...')

            file_stream.file = args[0]
            with open(args[0], 'x'):
                pass
            
            file_stream.init_skeleton()
            self.open(args = [args[0]])
        else:
            error(f'File [{args[0]}] already exists.')
    
    def fin(self):
        """ Method responsible for finishing htmldoc. """
        doc.content += '    {content}'
        if file_stream.open_bool:
            content_instance = file_stream.file_str.format(content = doc.content)
        else:
            content_instance = file_stream.file_str.format(title = doc.title, lang = doc.lang, char = doc.charset, author = doc.author, content = doc.content)

        with open(file_stream.file, 'w') as f:
            f.write(content_instance)

    def reload(self, args):
        """ Method that reloads current htmldoc with the new given elements. """
        print('Warning: You will not be able to change your changes later on.')
        print('Are you sure that you want to save these changes? (Y/N)')
        answer = input('           -> ')
        if answer.upper() == 'Y':
            print('Saving changes...')
            doc.content += '    {content}'
            if file_stream.open_bool:
                content_instance = file_stream.file_str.format(content = doc.content)
            else:
                content_instance = file_stream.file_str.format(title = doc.title, lang = doc.lang, char = doc.charset, author = doc.author, content = doc.content)

            with open(file_stream.file, 'w') as f:
                f.write(content_instance)
        
            print(f'Updated [{file_stream.file}]!')
            print(f'File [{file_stream.file}] attributes are not modifiable anymore.')
            print('^- Except: content')
        elif answer.upper() == 'N':
            print('Changes not saved.')
    #====================#

    #========Misc========#
    def out(self, args):
        """ CMD Output. """
        index_count = 0
        for arg in args:
            if not index_count == len(args)-1:
                print(arg, end=' ')
            else:
                print(arg) 
            index_count += 1

    def cls(self):
        """ Method that clears the commandline interface. """
        os.system('cls')
    
    def exit(self):
        """ Method that exits the program. """
        exit()
    
    def getfile(self):
        """ Method that outputs the current file. [See: @FileStream] """
        if len(file_stream.file) > 0:
            print('Current Working File: ', file_stream.file)
        else:
            print('Current Working File: NONE')
        file_stream.backup()
    #====================#

    #====HTMLDocInfo====#
    def title(self, args):
        """ Sets title for htmldoc. """
        doc.title = args[0]
        file_stream.backup()
    
    def charset(self, args):
        """ Sets charset for htmldoc. """
        doc.charset = args[0]
        file_stream.backup()

    def author(self, args):
        """ Sets author for htmldoc. """
        doc.author = args[0]
        file_stream.backup()

    def lang(self, args):
        """ Sets language for htmldoc. """
        doc.lang = args[0]
        file_stream.backup()
    #====================#

    #====FileEditing====#
    def coloring(self, args):
        if args[0].upper() == 'TRUE':
            print('wow')
            self.auto_coloring = True
        elif args[0].upper() == 'FALSE':
            print('not wow')
            self.auto_coloring = False
        else:
            print('XD')
            self.auto_color = args[0]       

    def header(self, args):
        """ Creates given header with given size in htmldoc. """
        # Command Info: (NOTE -> zero-indexed)
        # Arg1 = HeaderSize (index), Arg2 = Header Text
        try:
            if self.auto_coloring:
                color_str = self.auto_color
            else:
                try:
                    color_str = args[2]
                except Exception:
                    color_str = 'black'

            header_info = f'<h{args[0]} style="color:{color_str}";>{args[1]}</h{args[0]}>'
            append_content(header_info)

            print(f'Created HTML Document Element [{header_info}]')
            file_stream.backup()
        except IndexError:
            error(f'Command called takes more more than [{len(args)}] arguments')

    def paragraph(self, args):
        """ Creates a new paragraph with the given text. """
        # Command Info: (NOTE -> zero-indexed)
        # Arg1 = Paragraph Text
        if self.auto_coloring:
            color_str = self.auto_color
        else:
            try:
                color_str = args[1]
            except Exception:
                color_str = 'black'

        paragraph_str = f'<p style="color:{color_str}">{args[0]}</p>'
        append_content(paragraph_str)
        print(f'Created HTML Document Element [{paragraph_str}]')
        file_stream.backup()
    #=================#

    #===CommandAlternatives===#
    def h(self, args):
        """ Creates given header with given size in htmldoc. """
        # Command Info: (NOTE -> zero-indexed)
        # Arg1 = HeaderSize (index), Arg2 = Header Text
        # NOTE -> This is a alternative command [@method = header]
        try:
            if self.auto_coloring:
                color_str = self.auto_color
            else:
                try:
                    color_str = args[2]
                except Exception:
                    color_str = 'black'

            header_info = f'<h{args[0]} style="color:{color_str}";>{args[1]}</h{args[0]}>'
            append_content(header_info)

            print(f'Created HTML Document Element [{header_info}]')
            file_stream.backup()
        except IndexError:
            error(f'Command called takes more more than [{len(args)}] arguments')

    def p(self, args):
        """ Creates a new paragraph with the given text. """
        # Command Info: (NOTE -> zero-indexed)
        # Arg1 = Paragraph Text
        # NOTE -> This is a alternative command [@method = paragraph]
        if self.auto_coloring:
            color_str = self.auto_color
        else:
            try:
                color_str = args[1]
            except Exception:
                color_str = 'black'

        paragraph_str = f'<p style="color:{color_str}">{args[0]}</p>'
        append_content(paragraph_str)
        print(f'Created HTML Document Element [{paragraph_str}]')
        file_stream.backup()
    #=========================#


cmds = Commands()


class Commandline:
    """ Commandline Interface Environment Class. """
    def __init__(self):
        self.prefix: str = '-$'
    
    def change_prefix(self, new_prefix: str):
        """ Method that, you guessed it, changes the cmdl prefix. """
        self.prefix = new_prefix 
        
    def run(self):
        """ Method that runs the (runtime) endless cmd loop. """
        while 1:
            raw_cmd = input(f'{self.prefix} ').split()
            if not len(raw_cmd) == 0:
                base_cmd = raw_cmd[0]
                cmd_args = raw_cmd[1:]
                try:
                    no_check_func = ['cls', 'new', 'open', 'getfile', 'out', 'exit']
                    if base_cmd in no_check_func:
                        call_method(cmds, base_cmd, cmd_args)
                    else:
                        if len(file_stream.file) == 0:
                            error('FileStream file attribute is not defined')
                            print('| -> Create A File: "new file_name" - Open A File: "open file_name"')
                        else:
                            call_method(cmds, base_cmd, cmd_args)
                except AttributeError:
                    error(f'Command [{base_cmd}] could not be found.')
                except IndexError:
                    error(f'Command [{base_cmd}] called with wrong args -> index error')
                

# Commandline init
cmdl = Commandline()
cmdl.run()