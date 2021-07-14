# backgroundcolor = "#272822"  # "white"  # "#151515"
# forgroundcolor =  "#F8F8F2"  # "black"
familyset = "Courier New" # "Menlo"
transperence_level = 0.9
interpreterpath = "/Applications/Gismolang/"
interpreterfile = "gismo run "
config_editor = "nano"
fileExtensions = ".dyc"

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
    
    # ETC
    
    [r"[a-zA-Z0-9$]+[ \t]*(?=(\())", type_color, backgroundcolor, True, "", ""],
    [r"function[ \t]+[a-zA-Z0-9$]+", fn_color, backgroundcolor, True, "", ""],
    [r"override[ \t]+[a-zA-Z0-9$]+", fn_color, backgroundcolor, True, "", ""],
    
    # KEYWORDS
    [r"\yfunction\y", keyword_color, backgroundcolor, True, "italic", "italic"],
    [r"\yin\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\:=", keyword_color, backgroundcolor, True, "", ""],
    [r"\yis\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yrange\y", keyword_color, backgroundcolor, True, "italic", "italic"],
    [r"\yclaim\y", keyword_color, backgroundcolor, True, "italic", "italic"],
    [r"\ycase\y", keyword_color, backgroundcolor, True, "italic", "italic"],
    [r"\yif\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yelse\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yasync\y", keyword_color, backgroundcolor, True, "italic", "italic"],
    [r"\ysym\y", keyword_color, backgroundcolor, True, "italic", "italic"],
    [r"\yreturn\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yyield\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yundefined\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yinclude\y", keyword_color, backgroundcolor, True, "italic", "italic"],
    [r"\yfrom\y", keyword_color, backgroundcolor, True, "italic", "italic"],
    [r"\ytype\y", keyword_color, backgroundcolor, True, "italic", "italic"],
    [r"\yinner\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yabstract\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yoverride\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ypackage\y", keyword_color, backgroundcolor, True, "bold", "bold"],
    [r"\yconst\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yC\'s\y", keyword_color, backgroundcolor, True, "italic", "italic"],
    [r"\yinstanceof\y", keyword_color, backgroundcolor, True, "italic", "italic"],
    [r"\yrelease\y", keyword_color, backgroundcolor, True, "italic", "italic"],
    [r"\yend\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yor\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yand\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ythen\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ydefer\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ytypedef\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yself\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ynew\y", keyword_color, backgroundcolor, True, "", ""],
    [r"=>", keyword_color, backgroundcolor, True, "", ""],
    [r"->", keyword_color, backgroundcolor, True, "", ""],

    # String
    [r'"[^\"]*"', string_color, backgroundcolor, True, "", ""],

    # in String
    ["\\", "white", "red", False, "", ""], # Error \
    [r"\\\"", escape_color, backgroundcolor, True, "", ""],
    [r"\\\\", escape_color, backgroundcolor, True, "", ""],
    [r"\\t", escape_color, backgroundcolor, True, "", ""],
    [r"\\n", escape_color, backgroundcolor, True, "", ""],
    
    # Comments
    [r'#!.*',  keyword_color, backgroundcolor, True, "", ""],
    [r'--.*', comment_color, backgroundcolor, True, "", ""],
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
    "function",
    "function main (args)",
    "true",
    "false",
    "in",
    "in claim",
    "in range",
    "in case",
    "is",
    "claim",
    "range",
    "case",
    "undefined",
    "if",
    "else",
    "async",
    "sym",
    "return",
    "await",
    "yield",
    "include",
    "from",
    "type",
    "inner",
    "override",
    "abstact",
    "package",
    "C's",
    "then",
    "and",
    "or",
    "end",
    "defer",
    "self",
    "new",
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
