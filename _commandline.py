"""
This is the DocPy module made for creating HtmlDocuments in
a commandline interface environment.
It is also very handy for creating HTML Documentations.
"""

__author__ = 'Lotus'
__version__ = 0.6

# Imports
import os

# External Imports
try:
    from bs4 import BeautifulSoup
except ImportError as e:
    print('Error while trying to import external libary.')
    print('Traceback:\n', e)

# Create Back-up File
if not os.path.isfile(f'{os.getcwd()}/backup.txt'):
    with open('backup.txt', 'w'):
        pass

# Global Functions
def call_method(cls: object, function: str, args: list):
    """ Calls method from given class, with given arguments """
    getattr(cls, function)(args)

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
    background = ''


doc = Document()

# Global Function (includes mandatory object to work [doc | @Document])
def append_content(additional_content: str):
    """ Appends the content (@file = htmldoc, @tag = <body>). """
    doc.content += additional_content + '\n'


class FileStream:
    """ FileStream Class responsible for file handling. """
    def __init__(self):
        #====FileDataVars====#
        self.open_bool = False
        self.new_bool = False
        self.file = ''
        self.file_str = ''
        #====================#

        #===FileContentVar===#
        cwd = os.getcwd()
        try:
            with open(f'{cwd}/skeleton.html', 'r') as f:
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
        """ Gets the whole content of a given file. """
        with open(file_name, 'r') as f:
            return f.read()

    def backup(self):
        """ backs up the current htmldoc content in backup.txt """
        with open('backup.txt', 'w') as f:
            f.write(self.get_content(self.file))

    @staticmethod
    def insert_line(src: list, line: str, pos: int) -> list:
        """ Inserts line @pos in src [list]. """
        src = src[:pos] + [line] + src[pos:]
        return src

    def insert_content_tag(self, search_kw: str) -> bool:
        """ Method that inserts {content} before the </body> tag, if {content} is non existent. """
        content_tag = '  {content}'
        str_instance = self.file_str.splitlines()
        line_count = 0
        for line in str_instance:
            if not content_tag in line:
                if search_kw in line:
                    print('FOUND L')
                    str_instance = self.insert_line(
                                                    src = str_instance, 
                                                    line = content_tag, 
                                                    pos = line_count
                                                   )
                self.file_str = ''
                for line in str_instance:
                    self.file_str += line + '\n'

                with open(self.file, 'w') as f:
                    f.write(self.file_str)
            else:
                return
            line_count += 1

    def update_doc(self, src: str):
        """ Method that updates htmldoc with prettified HTML and inserted {config}. """
        with open(file_stream.file, 'w') as f:
            bs4_doc = BeautifulSoup(src, 'html.parser')
            f.write(bs4_doc.prettify())

        file_stream.insert_content_tag('</body>')

file_stream = FileStream()

class Commands:
    """ Commands class responsible for storing methods, that will get reflected. [See: C# Reflection] """
    def __init__(self):
        self.auto_coloring = True
        self.next_line = True
        self.auto_color = 'black'
    
    #====FileCommands====#
    def open(self, args):
        """ Method that opens the given file. """
        if not file_stream.new_bool:
            file_stream.open_bool = True

        cwd = os.getcwd()
        if os.path.isfile(f'{cwd}/{args[0]}'):
            file_stream.file = args[0]

            with open(file_stream.file, 'r') as f:
                file_stream.file_str = f.read()
            
            file_stream.insert_content_tag('</body>')
        else:
            error(f'Couldnt find [{args[0]}]')
        
        print(f'Opened [{args[0]}]!')

    def new(self, args):
        """ Method that creates a new file. """
        file_stream.new_bool = True
        cwd = os.getcwd()
        if not os.path.isfile(f'{cwd}/{args[0]}'):
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
        doc.content += '   {content }'
        if file_stream.open_bool:
            content_instance = file_stream.file_str.format(content = doc.content)
        else:
            content_instance = file_stream.file_str.format(
                                                        title = doc.title, 
                                                        lang = doc.lang, 
                                                        char = doc.charset, 
                                                        author = doc.author, 
                                                        content = doc.content
                                                        )

        with open(file_stream.file, 'w') as f:
            f.write(content_instance)

    def reload(self, args):
        """ Method that reloads current htmldoc with the new given elements. """
        print('Warning: You will not be able to change your changes later on.')
        print('Are you sure that you want to save these changes? (Y/N)')
        answer = input('           -> ')
        if answer.upper() == 'Y':
            print('Saving changes...')
            if file_stream.open_bool:
                content_instance = file_stream.file_str.format(content = doc.content)
                file_stream.update_doc(content_instance)
            else:
                content_instance = file_stream.file_str.format(
                                                           title = doc.title, 
                                                           lang = doc.lang, 
                                                           char = doc.charset, 
                                                           author = doc.author, 
                                                           content = doc.content,
                                                           background = doc.background
                                                           )
                file_stream.update_doc(content_instance)

            print(f'Updated [{file_stream.file}]!')
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

    def cls(self, args):
        """ Method that clears the commandline interface. """
        os.system('cls')
    
    def exit(self, args):
        """ Method that exits the program. """
        exit()
    
    def getfile(self, args):
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
    def background(self, args):
        """ Command that sets background color in htmldoc. """
        doc.background = args[0]

    def delete(self, args):
        """ Command that deletes everything in content. """
        print('Are you sure that you want to delete all of the <body> content? (Y/N)')
        answer = input('')
        if answer.upper() == 'Y':
            print('<body> content cleared!')
            doc.content = ''
        elif answer.upper() == 'N':
            print('<body> content not cleared.')

    def coloring(self, args):
        """ Command that auto-colors the given htmldoc element to the given color. """
        if args[0].upper() in ['TRUE', 'ON']:
            self.auto_coloring = True
            print('Auto-Coloring: On')
        elif args[0].upper() == ['FALSE', 'OFF']:
            self.auto_coloring = False
            print('Auto-Coloring: Off')
        else:
            self.auto_color = args[0]       
            print('Set auto-coloring to: [', args[0], ']')
            
    def code(self, args):
        """ Creates code tag with given content. """
        # Command Info: (NOTE -> zero-indexed)
        # Arg1 = CodeTagContent
        c_code, color_str = self._construct_txt(src = args, param_index = 0)
        
        code_content = f'<code style="color:{color_str}>{c_code}</code>'
        append_content(code_content)

        file_stream.backup()
    
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
    def c(self, args):
        """ Creates code tag with given content. """
        # Command Info: (NOTE -> zero-indexed)
        # Arg1 = CodeTagContent
        # NOTE -> This is a alternative version of the code method
        c_code, color_str = self._construct_txt(src = args, param_index = 0)
        
        code_content = f'<code style="color:{color_str}>{c_code}</code>'
        append_content(code_content)

        file_stream.backup()

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

    def ac(self, args):
        """ Command that auto-colors the given htmldoc element to the given color. """
        # NOTE -> This is a alternative version of the coloring method
        if args[0].upper() == 'TRUE':
            self.auto_coloring = True
            print('Auto-Coloring: On')
        elif args[0].upper() == 'FALSE':
            self.auto_coloring = False
            print('Auto-Coloring: Off')
        else:
            self.auto_color = args[0]
            print('Set auto-coloring to: [', args[0], ']')
    
    def bg(self, args):
        """ Command that sets background color in htmldoc. """
        # NOTE -> This is a alternative version of the background method
        doc.background = args[0]
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
        no_check_func = [
                        'cls', 
                        'new', 
                        'open', 
                        'getfile', 
                        'out', 
                        'exit', 
                        'coloring', 
                        'c',
                        'nextline']
        
        no_nextline_funcs = ['cls']
        
        while 1:
            raw_cmd = input(f'{self.prefix} ').split()
            if not len(raw_cmd) == 0:
                base_cmd = raw_cmd[0]
                cmd_args = raw_cmd[1:]
                try:
                    if base_cmd in no_check_func:
                        call_method(cmds, base_cmd, cmd_args)
                        if cmds.next_line:
                            if not base_cmd in no_nextline_funcs:
                                print()
                    else:
                        if len(file_stream.file) == 0:
                            error('FileStream file attribute is not defined')
                            print('| -> Create A File: "new file_name" - Open A File: "open file_name"')
                        else:
                            call_method(cmds, base_cmd, cmd_args)
                            if cmds.next_line:
                                if not base_cmd in no_nextline_funcs:
                                    print()
                except AttributeError:
                    error(f'Command [{base_cmd}] could not be found')
                except IndexError:
                    error(f'Command [{base_cmd}] requires more than the [{len(cmd_args)}] given arguments')

# Commandline init
cmdl = Commandline()
cmdl.run()
