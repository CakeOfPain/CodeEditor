# backgroundcolor = "#272822"  # "white"  # "#151515"
# forgroundcolor =  "#F8F8F2"  # "black"
familyset = "Menlo"
transperence_level = 0.9
interpreterpath = "C:\\GismoLang\\"
interpreterfile = "gismo run "
config_editor = "nano"
fileExtensions = ".gsm"

style = "light"


propetyWindow = Tk ()
propetyWindow.title ("Select Theme")
propetyWindow.eval('tk::PlaceWindow . center')

themes = [
	"light",
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

    [r"[0123456789]+", value_color, backgroundcolor, True, "", ""],
    [r"[0123456789]+u", value_color, backgroundcolor, True, "", ""],
    [r"[0123456789]+\.[0123456789]+", value_color, backgroundcolor, True, "", ""],
    [r"[A-Za-z]+[0123456789]+", forgroundcolor, backgroundcolor, True, "", ""],
    [r"[A-Za-z]+[0123456789]+\.[0123456789]*", forgroundcolor, backgroundcolor, True, "", ""],
    [r"\ytrue\y", value_color, backgroundcolor, True, "", ""],
    [r"\yfalse\y", value_color, backgroundcolor, True, "", ""],
    [r"\ynil\y", value_color, backgroundcolor, True, "", ""],

    [r'[A-Za-z0-9_$@]+[ \t]*(?=\()', type_color, backgroundcolor, True, "", ""],
    [r'[A-Za-z0-9_$@]+[ \t]*(?=(\(.*\{))', fn_color, backgroundcolor, True, "", ""],
    # [r"\(", forgroundcolor, backgroundcolor, True, "", ""],

    # Primitive Datatypes
    [r"\y[a-zA-Z_$]*\y *as *[a-zA-Z_$]*", type_color, backgroundcolor, True, "", ""],
    [r"\yas\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yis\y *[a-zA-Z_$]*", type_color, backgroundcolor, True, "", ""],
    [r"\yis\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yin\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yconst\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yrange\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yimplement\y *[a-zA-Z_$]*", fn_color, backgroundcolor, True, "", ""],
    [r"\yimplement\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ythis\y", keyword_color, backgroundcolor, True, "italic", "italic"],
    [r"\ynum\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\yCollection\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\ytxt\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\ylong\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\ydouble\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\yulong\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\yint\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\yuint\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\yfloat\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\yushort\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\yshort\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\ybyte\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\yany\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\yubyte\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\yRef\y", type_color, backgroundcolor, True, "italic", "italic"],
    [r"\yunion\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ywhile\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ybreak\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ycontinue\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yif\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yelse\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\yvanguard\y", keyword_color, backgroundcolor, True, "", ""],
    [r"\ytype\y", keyword_color, backgroundcolor, True, "italic", "italic"],
    [r"\yundefined\y", keyword_color, backgroundcolor, True, "italic", "italic"],

    #TEMP
    # [r"\yfn\y", keyword_color, backgroundcolor, True, "", ""],
    # [r"\yfunc\y", keyword_color, backgroundcolor, True, "", ""],
    # [r"\yfunction\y", keyword_color, backgroundcolor, True, "", ""],

    [r"\yreturn\y", keyword_color, backgroundcolor, True, "", ""],
    
    [r"@[A-Za-z0-9_$@]+", comment_color, backgroundcolor, True, "", ""],
    [r"#", keyword_color, backgroundcolor, True, "", ""],

    # String
    [r'"[^\"]*"', string_color, backgroundcolor, True, "", ""],

    # in String
    ["\\", "white", "red", False, "", ""], # Error \
    [r"\\\"", escape_color, backgroundcolor, True, "", ""],
    [r"\\\\", escape_color, backgroundcolor, True, "", ""],
    [r"\\t", escape_color, backgroundcolor, True, "", ""],
    [r"\\n", escape_color, backgroundcolor, True, "", ""],
    
    # Comments
    [r'//.*', comment_color, backgroundcolor, True, "", ""]
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

bluePrints = [
    ("Graphics Application", 
"""
windowTitle: "My Graphics App"
windowWidth = 600
windowHeight = 400

vanguard begin (txt[] args) {
    setup@sdl ()
    init@graphics (windowTitle, windowWidth, windowHeight, 1)
}

initApp (Ref window, Ref renderer) {
    window.center@sdl ()
    clearDisplay@graphics ()
}

cleanUp (Ref window, Ref renderer) {

}

drawImages (Ref renderer) {

}

onQuit () {
    stop@graphics ()
}

onKeyDown (Ref keycode, Ref mousebutton) {

}

onKeyUp (Ref keycode, Ref mousebutton) {

}

onMouseWheelMotion (long x, long y) {

}

update (Ref window) {

}

draw (Ref renderer) {

}
""")
]

suggestionsListBase = [
    "vanguard",
    "vanguard begin(txt[] args)",
    "while",
    "if",
    "else",
    "is",
    "as",
    "output (",
    "input (",
    ".Println ()",
    ".Print ()",
    ".Length ()",
    ".Size ()",
    "exit (",
    "type (",
    ".ChatAt (",
    ".InsertChar (",
    "const",
    "in",
    "range",
    "implement",
    "this",
    "return",
    "txt",
    "long",
    "double",
    "ulong",
    "int",
    "uint",
    "float",
    "ushort",
    "short",
    "byte",
    "ubyte",
    "Ref",
    "break",
    "continue",
    "undefined",
    "true",
    "false",
    "@std",
    "@sdl",
    "@graphics",
    "@math",
    "@calc",
    "@graph",
    "@os",
    "eval@calc (",
    "File@File (",
    ".GetContentOfFile@File (",
    ".GetPathOfFile@File (",
    ".DoesFileExist@File (",
    ".setScale@graph (",
    ".setBackgroundColor@graph (",
    ".setForgroundColor@graph (",
    "initGraph@graph (",
    ".drawPoints@graph (",
    ".showGraph@graph (",
    ".mainloop@graph (",
    "closeGraph@graph (",
    "stop@graphics ()",
    "clearDisplay@graphics ()",
    "init@graphics (",
    "abs@math (",
    "div_quot@math (",
    "div_rem@math (",
    "sin@math (",
    "cos@math (",
    "tan@math (",
    "asin@math (",
    "acos@math (",
    "sinh@math (",
    "cosh@math (",
    "tanh@math (",
    "fmod@math (",
    "cosf@math (",
    "asinh@math (",
    "acosh@math (",
    "atanh@math (",
    "exp2@math (",
    "expm1@math (",
    "ilogb@math (",
    "logb@math (",
    "log1p@math (",
    "log2p@math (",
    "cbrt@math (",
    "hypot@math (",
    "remainder@math (",
    "fdim@math (",
    "fmin@math (",
    "fmax@math (",
    "trunc@math (",
    "rint@math (",
    "lrint@math (",
    "llrint@math (",
    "round@math (",
    "lround@math (",
    "llround@math (",
    "nearbyint@math (",
    "nextafter@math (",
    "nexttoward@math (",
    "copysign@math (",
    "scalbn@math (",
    "scalbln@math (",
    "fma@math (",
    "tgamma@math",
    "lgamma@math",
    "erf@math (",
    "erfc@math (",
    "floor@math (",
    "trand@math ()",
    "sqrt@math (",
    "pow@math (",
    "random@math (",
    "open@os (",
    ".close@os ()",
    ".read@os ()",
    ".write@os (",
    "alert@os (",
    "inform@os (",
    "warn@os (",
    "tell@os (",
    "system@os (",
    "fontColor@os (",
    "cursorPos@os (",
    "beep@os (",
    "wait@os (",
    "formUShort@os (",
    "formUInt@os (",
    "formULong@os (",
    ".shR@os (",
    ".shL@os (",
    ".bitAt@os (",
    ".bitSet@os (",
    "unsigned@os (",
    "signed@os (",
    "setup@sdl ()",
    "quit@sdl ()",
    "delay@sdl (",
    "createWindow@sdl ()",
    ".setTitle@sdl (",
    ".setSize@sdl (",
    ".getWidth@sdl ()",
    ".getHeight@sdl ()",
    ".show@sdl ()",
    ".hide@sdl ()",
    ".destroyWindow@sdl ()",
    ".checkEvent@sdl ()",
    "readKeyUpEvent@sdl ()",
    "readKeyDownEvent@sdl ()",
    "readMouseButtonDownEvent@sdl ()",
    "readMouseButtonUpEvent@sdl ()",
    "readMouseWheelX@sdl ()",
    "readMouseWheelY@sdl ()",
    "getMouseX@sdl ()",
    "getMouseY@sdl ()",
    ".center@sdl ()",
    ".fullscreen@sdl (",
    ".resizable@sdl (",
    "getMouseMotion@sdl ()",
    ".createRenderer@sdl ()",
    ".clearRenderer@sdl ()",
    ".drawPixel@sdl (",
    ".drawRect@sdl (",
    ".fillRect@sdl (",
    ".drawLine@sdl (",
    ".drawColor@sdl (",
    ".present@sdl ()",
    "destroyRenderer@sdl ()",
    ".loadImage@sdl (",
    ".destroyImage@sdl ()",
    ".drawImage@sdl (",
    ".widthOfImage@sdl ()",
    ".heightOfImage@sdl ()",
    ".drawSprite@sdl (",
    "getPerformanceCounter@sdl ()",
    "getPerformanceFrequency@sdl ()",
    "translate@sdl (",
    "translate_add@sdl (",
    "translate_x@sdl (",
    "translate_y@sdl (",
    "translation_x@sdl ()",
    "translation_y@sdl ()",
    ".drawTo@sdl (",
    ".emptyImage@sdl (",
    ".isKeyDown@sdl ()",
    ".isKeyUp@sdl ()",
    ".drawCircle@sdl (",
    ".fillCircle@sdl ("
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
