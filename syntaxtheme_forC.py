# backgroundcolor = "#272822"  # "white"  # "#151515"
# forgroundcolor =  "#F8F8F2"  # "black"
familyset = "Menlo"
transperence_level = 0.9
interpreterpath = "/Applications/Gismolang/"
interpreterfile = "gismo run "
config_editor = "nano"
fileExtensions = ".c"

style = "light"


propetyWindow = Tk ()
propetyWindow.title ("Select Theme")
propetyWindow.eval('tk::PlaceWindow . center')

themes = [
	"light",
    "light #2",
	"dark",
	"highcontrast"
] 

themesView = StringVar (propetyWindow)
themesView.set (themes[0])

opt = OptionMenu (propetyWindow, themesView, *themes)
opt.config (width=20, font=(familyset, 12))
opt.pack ()

button = Button (
	propetyWindow, 
	text="continue", 
	width=24, font=("Menlo", 12), 
	command=propetyWindow.destroy
)
button.pack ()

propetyWindow.mainloop ()

style = themesView.get()


if style == "dark":
    backgroundcolor = "#272822"
    forgroundcolor =  "#F8F8F2"
    keyword_color =  "#F92672"
    type_color =   "#66D9EF"
    value_color =  "#AE81FF"
    fn_color =  "#A6E22E"
    string_color =  "#E6DB74"
    escape_color = "#FD971F"
    comment_color = "#75715E"
    lineMarkColor = "#171812"

if style == "light":
    backgroundcolor = "white" # "#EEE"
    forgroundcolor =  "black"
    keyword_color =  "blue"
    type_color =   "purple"
    value_color =  "dark red"
    fn_color =  "dark cyan"
    string_color =  "dark blue"
    escape_color = "green"
    comment_color = "gray"
    lineMarkColor = "#F8F8F8"

if style == "light #2":
    backgroundcolor = "white" # "#EEE"
    forgroundcolor =  "black"
    keyword_color =  "purple"
    type_color =   "#006680"
    value_color =  "dark red"
    fn_color =  "#483d8b"
    string_color =  "dark blue"
    escape_color = "green"
    comment_color = "gray"
    lineMarkColor = "#F8F8F8"

if style == "highcontrast":
    backgroundcolor = "#000" # "#EEE"
    forgroundcolor =  "#FFF"
    keyword_color =  "#f000ff"
    type_color =   "#4deeea"
    value_color =  "#FF6600"
    fn_color =  "#74ee15"
    string_color =  "#E6FB04"
    escape_color = "#4deeea"
    comment_color = "gray"
    lineMarkColor = "#111"


highlight = [

    # VALUES
    [r"[0123456789]+", value_color, backgroundcolor, True, "", ""],
    [r"[0123456789]+u", value_color, backgroundcolor, True, "", ""],
    [r"[0123456789]+\.[0123456789]+", value_color, backgroundcolor, True, "", ""],
    [r"[A-Za-z]+[0123456789]+", forgroundcolor, backgroundcolor, True, "", ""],
    [r"[A-Za-z]+[0123456789]+\.[0123456789]*", forgroundcolor, backgroundcolor, True, "", ""],
    [r"\ytrue\y", value_color, backgroundcolor, True, "", ""],
    [r"\yfalse\y", value_color, backgroundcolor, True, "", ""],
    [r"\yNULL\y", value_color, backgroundcolor, True, "", ""],
    [r"\ynullptr\y", value_color, backgroundcolor, True, "", ""],
    
    # ETC
    
    [r"[a-zA-Z$_][a-zA-Z0-9$_]*[ \t]*(?=(\())", type_color, backgroundcolor, True, "", ""],
    [r"[a-zA-Z$_][a-zA-Z0-9$_]*[ \t]+[a-zA-Z$_][a-zA-Z0-9$_]*", fn_color, backgroundcolor, True, "", ""],
    
    # TYPES

    [r"\ychar\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\ydouble\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\yfloat\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\yint\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\ylong\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\yshort\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\y_Bool\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\y_Complex\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\y_Imaginary\y", type_color, backgroundcolor, True, "italic", "italic"],

    # KEYWORDS
    [r"\yauto\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ybreak\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ycase\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yconst\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ycontinue\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ydefault\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ydo\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yelse\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yenum\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yextern\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yfor\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ygoto\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yif\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yinline\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yregister\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yrestrict\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yreturn\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ysigned\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ysizeof\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ystatic\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ystruct\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yswitch\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ytypedef\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yunion\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yunsigned\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yvoid\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yvolatile\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ywhile\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\y_Alignas\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\y_Alignof\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\y_Atomic\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\y_Noreturn\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\y_Static_assert\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\y_Thread_local\y", keyword_color, backgroundcolor, True, "", ""],

    # Preprocessor directives
    [r"#include", keyword_color, backgroundcolor, True, "", ""],
    [r"#define", keyword_color, backgroundcolor, True, "", ""],
    [r"#undefine", keyword_color, backgroundcolor, True, "", ""],
    [r"#ifndef", keyword_color, backgroundcolor, True, "", ""],
    [r"#ifdef", keyword_color, backgroundcolor, True, "", ""],
    [r"#endif", keyword_color, backgroundcolor, True, "", ""],

    # String
    [r'"[^\"]*"', string_color, backgroundcolor, True, "", ""],

    # in String
    ["\\", "white", "red", False, "", ""], # Error \
    [r"\\\"", escape_color, backgroundcolor, True, "", ""],
    [r"\\\\", escape_color, backgroundcolor, True, "", ""],
    [r"\\t", escape_color, backgroundcolor, True, "", ""],
    [r"\\n", escape_color, backgroundcolor, True, "", ""],
    
    # Comments
    [r'/\*(.|\n|[^(\*/)])*\*/',  comment_color, backgroundcolor, True, "", ""],
    [r'//.*', comment_color, backgroundcolor, True, "", ""],
]

# simplify's higlight


simple = []
before = None
for x in highlight:
	if x[3] == backgroundcolor:
		x[3] = ""
	if before is None:
		before = x
		simple.append(x)
	else:
		if before[1] == x[1] and before[2] == x[2] and before[3] == x[3] and before[4] == x[4]:
			simple[-1][0] += "|" + x[0]
		else:
            		before = x
            		simple.append(x)
highlight = simple
del simple
del before

bluePrints = []

suggestionsListBase = [
    "auto",
    "break",
    "case",
    "char",
    "const",
    "continue",
    "default",
    "do",
    "double",
    "else",
    "enum",
    "extern",
    "float",
    "for",
    "goto",
    "if",
    "inline",
    "int",
    "long",
    "register",
    "restrict",
    "return",
    "short",
    "signed",
    "sizeof",
    "static",
    "struct",
    "switch",
    "typedef",
    "union",
    "unsigned",
    "void",
    "volatile",
    "while",
    "#include",
    "#define",
    "#undefine"
    "#ifndef",
    "#ifdef",
    "#endif",
    "NULL",
    "nullptr",
]

suggestionsList = suggestionsListBase

"""

gpath = ""
variables = []

#import threading
import subprocess
import threading
import time

gRunning = True

def getVariables (path):
    global suggestionsList
    global suggestionsListBase
    global variables
    global gpath
    gpath = path
    suggestionsList = suggestionsListBase + variables

def gcomp (name):
    global gpath
    global variables
    while gRunning:
        if gpath != "":
            result = subprocess.run (["gismo", "globals", gpath], shell=True ,stdout=subprocess.PIPE)
            tvariables = result.stdout.decode('utf-8').split(";")
            variables = tvariables[0:len(tvariables)]
        time.sleep (300 / 1000)

def gOnEnding ():
    global gcomp_thr
    global gRunning
    gRunning = False
onEnding = gOnEnding

gcomp_thr = threading.Thread(target=gcomp, args=(1,))
gcomp_thr.start()

onButtonChange = getVariables
"""
